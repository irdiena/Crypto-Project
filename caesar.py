def caesar_cipher(text, key, mode='encrypt'):
    """
    Encrypts or decrypts text using a Caesar Cipher.
    text: The input string (plaintext or ciphertext)
    key: An integer representing the shift value
    mode: 'encrypt' or 'decrypt'
    """
    result = ""
    
    # If decrypting simply reverse the shift direction
    if mode == 'decrypt':
        key = -key
        
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine if  uppercase or lowercase ASCII bases
            shift_base = ord('A') if char.isupper() else ord('a')
            # Perform the shift and wrap around the alphabet using modulo 26
            shifted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            result += shifted_char
        else:
            result += char
            
    return result

# Testing the Caesar Cipher
print("--- Substitution (Caesar) Cipher ---")
plaintext_sub = "SECURE MESSAGE"
key_sub = 5

encrypted_sub = caesar_cipher(plaintext_sub, key_sub, mode='encrypt')
decrypted_sub = caesar_cipher(encrypted_sub, key_sub, mode='decrypt')

print(f"Plaintext:  {plaintext_sub}")
print(f"Encrypted:  {encrypted_sub}")
print(f"Decrypted:  {decrypted_sub}\n")

