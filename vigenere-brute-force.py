### Vigenere Cipher Brute Force

import string
import itertools

def vigenere_cipher(message, key_length):
    message = message.replace(" ","").upper()
    alphabet = list(string.ascii_uppercase)

    print(f"Original message: \t{message}")

    possible_keys = []
    for i in range(key_length):
        possible_keys += itertools.combinations_with_replacement(alphabet, key_length)

    for possible_key in possible_keys:
        key_encrypted = []
        for char in possible_key:
            key_encrypted.append(alphabet.index(char))

        key_array = []
        key_array = key_encrypted * int(len(message) / key_length) + key_encrypted[:int(len(message) % key_length)]

        message_decrypted = ""

        for char_message, key_char in zip(message, key_array):
            char_index = alphabet.index(char_message)
            char_decrypted = char_index - key_char
            message_decrypted += alphabet[char_decrypted]

        print(f"Key: {possible_key}")
        print(f"Key Encrypted: {key_encrypted}")
        print(f"Decrypted message: \t{message_decrypted}")


if __name__ == '__main__':
    print("Welcome to Vigenere Brute Force Decrypter")
    message = input("Enter your message: ")                 # NIVU QV JR DTTS ULIFI FOI KIVVF
    key_length = int(input("Enter your key length: "))
    vigenere_cipher(message, key_length)

