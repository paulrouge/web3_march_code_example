from cryptography.fernet import Fernet


def encrypt_string(password, plaintext):
    key = password.encode('utf-8')
    f = Fernet(key)
    ciphertext = f.encrypt(plaintext.encode('utf-8'))
    return ciphertext.hex()

# Example usage:
password = 'mysecretpassword'
plaintext = 'Hello, world!'
encrypted_string = encrypt_string(password, plaintext)
print(encrypted_string)
