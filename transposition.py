import math

def columnar_encrypt(text, key):
    """Encrypts text using Columnar Transposition."""
    ciphertext = ""
    # Track the alphabetical index of each character in the key
    k_index = 0
    text_len = float(len(text))
    text_list = list(text)
    key_list = sorted(list(key))
    
    # Calculate columns and rows for the grid
    col = len(key)
    row = int(math.ceil(text_len / col))
    
    # Add padding (e.g., '_') to fill the empty grid cells if necessary
    fill_null = int((row * col) - text_len)
    text_list.extend('_' * fill_null)
    
    # Create the grid and read columns alphabetically based on the key
    matrix = [text_list[i: i + col] for i in range(0, len(text_list), col)]
    
    for _ in range(col):
        curr_idx = key.index(key_list[k_index])
        ciphertext += ''.join([row[curr_idx] for row in matrix])
        # Mark used key character to handle duplicate letters in the key
        key = key.replace(key[curr_idx], '_', 1)
        k_index += 1
        
    return ciphertext

def columnar_decrypt(ciphertext, key):
    """Decrypts text using Columnar Transposition."""
    plaintext = ""
    k_index = 0
    
    # Track column and row counts
    col = len(key)
    row = int(math.ceil(len(ciphertext) / col))
    key_list = sorted(list(key))
    
    # Create an empty grid
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
        
    # Reconstruct the grid column by column
    ptr = 0
    for _ in range(col):
        curr_idx = key.index(key_list[k_index])
        for j in range(row):
            dec_cipher[j][curr_idx] = ciphertext[ptr]
            ptr += 1
        key = key.replace(key[curr_idx], '_', 1)
        k_index += 1
        
    # Read the grid row by row to get the plaintext
    plaintext = ''.join(sum(dec_cipher, []))
    # Remove the padding added during encryption
    return plaintext.rstrip('_')

# Testing the Columnar Transposition Cipher
print("--- Transposition (Columnar) Cipher ---")
plaintext_trans = "CONFIDENTIAL DATA"
key_trans = "HACK"

encrypted_trans = columnar_encrypt(plaintext_trans, key_trans)
decrypted_trans = columnar_decrypt(encrypted_trans, key_trans)

print(f"Plaintext:  {plaintext_trans}")
print(f"Key:        {key_trans}")
print(f"Encrypted:  {encrypted_trans}")
print(f"Decrypted:  {decrypted_trans}")

