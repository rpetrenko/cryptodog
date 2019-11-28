from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii


def generate_rsa_keys():
    """
    encrypted = pow( ord('a'), e, p*q )
    decrypted = chr( pow(encrypted, d, p*q) )
    :return:
    """
    key_pair = RSA.generate(2048)

    public_key = key_pair.publickey()
    public_key_PEM = public_key.exportKey()
    private_key_PEM = key_pair.exportKey()
    print("p={}".format(key_pair.p))
    print("q={}".format(key_pair.q))
    print("n=pq", key_pair.n)
    print("e=", public_key.e)
    print("d={}".format(key_pair.d))
    print("")
    print("Public key (n):", hex(public_key.n))
    print("Public key (e):", hex(public_key.e))
    print("Public key PEM:")
    print(public_key_PEM.decode('ascii'))
    print("")
    print("Private key (n):", hex(public_key.n))
    print("Private key (d):", hex(key_pair.d))
    print("Private key PEM")
    print(private_key_PEM.decode('ascii'))
    print("")
    return public_key, key_pair


def encrypt(msg, public_key):
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(msg)
    return encrypted


def decrypt(msg, key_pair):
    decryptor = PKCS1_OAEP.new(key_pair)
    decrypted = decryptor.decrypt(msg)
    return decrypted


if __name__ == "__main__":
    print("=== Generate key pair")
    public_key, key_pair = generate_rsa_keys()
    msg = b'a'*128
    print("=== Message to encrypt: {}".format(msg))
    encrypted_msg = encrypt(msg, public_key)
    print("=== Encrypted msg:", binascii.hexlify(encrypted_msg))
    decrypted_msg = decrypt(encrypted_msg, key_pair)
    print("=== Decrypted msg:", decrypted_msg)
