

class Caesar(object):

    def __init__(self, shift):
        self.shift = shift

    def _shift(self, letter, shift):
        inum = ord(letter) - ord('a')
        new_inum = (inum + shift) % 26
        return chr(ord('a') + new_inum)

    def encrypt(self, text):
        text = text.lower()
        res = ""
        for a in text:
            if a.isalpha():
                res += self._shift(a, self.shift)
        return res

    def decrypt(self, text):
        res = ""
        for a in text:
            res += self._shift(a, -self.shift)
        return res


if __name__ == "__main__":
    c = Caesar(2)
    text = "Hello, Diana!"
    encrypted = c.encrypt(text)
    print("Original  [{}]".format(text))
    print("Encrypted [{}]".format(encrypted))
    decrypted = c.decrypt(encrypted)
    print("Decrypted [{}]".format(decrypted))