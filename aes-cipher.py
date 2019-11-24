from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import json


# secret key should be available on both sides
SECRET_KEY = b'Sixteen byte key'

# data structure used by both
JSON_KEYS = ['nonce', 'header', 'msg', 'tag']


def encrypt_and_send(msg, header=b'header'):
    cipher = AES.new(SECRET_KEY, AES.MODE_EAX)
    cipher.update(header)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg)
    json_v = [b64encode(x).decode('utf-8') for x in [nonce, header, ciphertext, tag]]
    result = json.dumps(dict(zip(JSON_KEYS, json_v)))
    return result


def receive_and_decrypt(data_json):
    # receiver
    try:
        b64 = json.loads(data_json)
        jv = {k:b64decode(b64[k]) for k in JSON_KEYS}

        cipher = AES.new(SECRET_KEY, AES.MODE_EAX, nonce=jv['nonce'])
        cipher.update(jv['header'])
        plaintext = cipher.decrypt_and_verify(jv['msg'], jv['tag'])
        print("The message is authentic: {}".format(plaintext))
    except (ValueError, KeyError):
        print("Key incorrect or message corrupted")


data = encrypt_and_send(b"secret")
print("Sending data {}".format(data))
receive_and_decrypt(data)
