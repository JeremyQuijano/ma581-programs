### Vigenere Cipher

### Shift Ciper Program
import string

def vigenere_cipher(message, key, method):
    message = message.replace(" ","").upper()
    key = key.upper()
    alphabet = list(string.ascii_uppercase)

    # alphabet_encrypt = alphabet[key:] + alphabet[:key]
    # alphabet_decrypt = alphabet[-key:] + alphabet[:-key]
    message_encrypted = ""
    message_decrypted = ""

    print(f"Original message: \t{message}")

    key_encrypted = []
    for char in key:
        key_encrypted.append(alphabet.index(char))

    key_array = []
    key_array = key_encrypted * int(len(message) / len(key)) + key_encrypted[:int(len(message) % len(key))]

    if method.lower() == "encrypt":
        for char_message, key_char in zip(message, key_array):
            char_index = alphabet.index(char_message)
            char_decrypted = (char_index + key_char) % len(alphabet)
            message_encrypted += alphabet[char_decrypted]
        print(f"Encrypted message: \t{message_encrypted}")

    elif method.lower() == "decrypt":
        for char_message, key_char in zip(message, key_array):
            char_index = alphabet.index(char_message)
            char_decrypted = char_index - key_char
            message_decrypted += alphabet[char_decrypted]
        print(f"Decrypted message: \t{message_decrypted}")

if __name__ == '__main__':
    print("Welcome to Vigenere Cipher")
    message = input("Enter your message: ")     # NIVU QV JR DTTS ULIFI FOI KIVVF
    key = input("Enter your key: ")
    method = input("Enter your method (Encrypt/Decrypt): ")
    vigenere_cipher(message, key, method)

