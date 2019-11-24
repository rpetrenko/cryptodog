import hashlib

msg = b"HELLO"

# md5 hash
m = hashlib.md5()
m.update(msg)
print("md5: {}".format(m.hexdigest()))

# SHA-1 hashes
m = hashlib.sha1()
m.update(msg)
print("sha1: {}".format(m.hexdigest()))

# SHA-2 hashes
m = hashlib.sha256()
m.update(msg)
print("sha256: {}".format(m.hexdigest()))

m = hashlib.sha512()
m.update(msg)
print("sha512: {}".format(m.hexdigest()))

# windows uses md4 and unicode
msg = "P@sw0rd"
m = hashlib.new('md4')
m.update(msg.encode('utf-16le'))
print("Windows: [{}]; hashed(md4): {}".format(msg, m.hexdigest()))