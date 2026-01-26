### Shift Ciper Program
import string

def shift_cipher(message, key, method):
    message = message.upper()
    alphabet = list(string.ascii_uppercase)
    alphabet_encrypt = alphabet[key:] + alphabet[:key]
    alphabet_decrypt = alphabet[-key:] + alphabet[:-key]
    message_encrypted = ""
    message_decrypted = ""

    print(f"Original message: {message}")

    if method.lower() == "encrypt":
        for char in message:
            char_index = alphabet.index(char)
            message_encrypted += alphabet_encrypt[char_index]
        print(f"Encrypted message: {message_encrypted}")

    elif method.lower() == "decrypt":
        for char in message:
            char_index = alphabet.index(char)
            message_decrypted += alphabet_decrypt[char_index]
        print(f"Decrypted message: {message_decrypted}")

if __name__ == '__main__':
    shift_cipher('dhnyvgl', 13, 'decrypt')

