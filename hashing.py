import hashlib
from passlib.hash import sha512_crypt


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

# linux passwords (check /etc/login.defs for the ENCRYPT_METHOD and the number of rounds, 5000 default)
# then check output of /etc/shadow
# split string by : and take first two elements
# first element is username, second is pass
# split pass by $ symbol and take the second element, that will be salt
# the first element is the password type, usually equals to 6
# use this salt + rounds + password to can hashed password shown in /etc/shadow
salt = "ABC"
password = msg
print("Salt={}, password={}".format(salt, password))
hashed = sha512_crypt.using(salt=salt, rounds=5000).hash(password)
print("Linux hashed password: {}".format(hashed))

