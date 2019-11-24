"""
XOR

0^0 = 0
1^0 = 1
0^1 = 1
1^1 = 0

if key is less then the message just keep repeating it
encode ABC with B key
ABC:   0b 0100 0001 | 0100 0010 | 0100 0011
B-rep: 0b 0100 0010 | 0100 0010 | 0100 0010
XOR:   0b 0000 0011 | 0000 0000 | 0000 0001

"""
import binascii


class XorEncoder(object):
    def __init__(self, key):
        self.key = key

    def encode(self, msg):
        """
        encode with XOR
        :param msg:
        :return: binary representation of encoding
        """
        res = ""
        for i, a in enumerate(msg):
            k = self.key[i % len(self.key)]
            x = ord(k) ^ ord(a)
            res += chr(x)
        return res.encode('utf-8')

    def decode(self, msg):
        """
        with XOR double encoding returns the original message
        :param msg:
        :return: decoded message
        """
        return self.encode(msg.decode('utf-8'))


if __name__ == "__main__":
    c = XorEncoder("qrs")
    text = "HELLO Kitty"
    encoded = c.encode(text)
    print("Original {}".format(text))
    print("Encoded bin {}".format(encoded))
    print("Encoded hex {}".format(binascii.hexlify(encoded)))
    decoded = c.decode(encoded)
    print("Decoded {}".format(decoded))

