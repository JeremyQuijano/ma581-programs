### Substitution Cipher Breaker

import string

def substitution_cipher_breaker(message):
    message = message.replace(" ","").upper()
    key = list(string.ascii_uppercase)
    alphabet = list(string.ascii_uppercase)

    message_encrypted = ""
    message_decrypted = ""

    print(f"Original message: \t{message}")

    key_encrypted = []
    for char in key:
        key_encrypted.append(alphabet.index(char))

    key_array = []
    key_array = key_encrypted * int(len(message) / len(key)) + key_encrypted[:int(len(message) % len(key))]

    for char_message, key_char in zip(message, key_array):
        char_index = alphabet.index(char_message)
        char_decrypted = char_index - key_char
        message_decrypted += alphabet[char_decrypted]
    print(f"Decrypted message: \t{message_decrypted}")

if __name__ == '__main__':
    print("Welcome to Substitution Cipher")
    message = input("Enter your message: ")     # WHCUHFWXOWHUQXOMOMQVSQWAMWHCUHFXOLNWXQMQVSQWAWMQLN
    substitution_cipher_breaker(message)

