def rc4(key, data):
    S = list(range(256))
    j = 0
    key_length = len(key)

    # KSA
    for i in range(256):
        j = (j + S[i] + ord(key[i % key_length])) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA
    i = 0
    j = 0
    result = []

    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        result.append(byte ^ K)

    return result


def text_to_bytes(text):
    return [ord(c) for c in text]


def bytes_to_text(byte_list):
    return ''.join(chr(b) for b in byte_list)


def to_hex(data):
    return ''.join(f'{b:02X}' for b in data)


def from_hex(hex_str):
    return [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]


# 🔹 User Input
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

# 🔹 Encryption
plaintext_bytes = text_to_bytes(plaintext)
encrypted_bytes = rc4(key, plaintext_bytes)
hex_encrypted = to_hex(encrypted_bytes)

# 🔹 Decryption
cipher_bytes = from_hex(hex_encrypted)
decrypted_bytes = rc4(key, cipher_bytes)
decrypted_text = bytes_to_text(decrypted_bytes)

# 🔹 Output
print("\n--- RC4 Result ---")
print("Plaintext:", plaintext)
print("Key:", key)
print("Encrypted (HEX):", hex_encrypted)
print("Decrypted:", decrypted_text)
print("\n")