from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

def aes_encrypt(plaintext, key):
    # AES needs an Initialization Vector (IV) for CBC mode to make it secure
    iv = get_random_bytes(16)
    
    # Create the AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # AES requires data to be in 128-bit (16 byte) blocks. 
    # Use 'pad' to add extra bytes if the text doesn't fit exactly.
    padded_data = pad(plaintext.encode(), AES.block_size)
    
    # Encrypt the padded data
    ciphertext = cipher.encrypt(padded_data)
    
    return iv, ciphertext

def aes_decrypt(iv, ciphertext, key):
    # Create the cipher object again with the same key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the data
    decrypted_padded_data = cipher.decrypt(ciphertext)
    
    # Remove the extra padding bytes added during encryption
    plaintext = unpad(decrypted_padded_data, AES.block_size).decode()
    
    return plaintext

# Main Program Execution 
if __name__ == "__main__":
    print("=== AES-128 Block Cipher ===")
    
    # AES-128 requires exactly a 16-byte (128-bit) key.
    key = b"MySecretKey12345" # Exactly 16 characters
    
    # Ask the user for input
    message = input("Enter plaintext: ")
    
    # Encrypt the message
    iv, encrypted_msg = aes_encrypt(message, key)
    
    # Convert to HEX so it is readable on the screen (instead of weird symbols)
    iv_hex = binascii.hexlify(iv).decode()
    encrypted_hex = binascii.hexlify(encrypted_msg).decode()
    
    # Decrypt the message back
    decrypted_msg = aes_decrypt(iv, encrypted_msg, key)
    
    # Display the results
    print("\nAES Result")
    print(f"Plaintext: {message}")
    print(f"Key: {key.decode()}")
    print(f"IV (HEX): {iv_hex}")
    print(f"Encrypted (HEX): {encrypted_hex}")
    print(f"Decrypted: {decrypted_msg}")
    print("\n")