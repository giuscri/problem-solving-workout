from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt(bs, k):
    cipher = Cipher(algorithms.AES(k), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(bs) + decryptor.finalize()

def encrypt(bs, k):
    cipher = Cipher(algorithms.AES(k), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(bs) + encryptor.finalize()

if __name__ == '__main__': pass
