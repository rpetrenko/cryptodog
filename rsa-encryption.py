"""
Not practical to encode large messages with RSA. A better approach is
to use RSA to send AES key and then encode everything with AES

Choose primes from http://my.core.com/~katiemarie10/prime/prime1-1G.htm

Output:
p 557 q 1777
p*q 989789
e 65537 phi 987456
public (e, n)(65537, 989789)
private(d, n)(1336577, 989789)
original msg 012
ords [48, 49, 50]
calculating x**e % n
48**65537 % 989789 = 424495
calculating x**e % n
49**65537 % 989789 = 860932
calculating x**e % n
50**65537 % 989789 = 278537
encrypted [424495, 860932, 278537]
calculating y**d % n
424495**1336577 % 989789 = 48
got char 0
calculating y**d % n
860932**1336577 % 989789 = 49
got char 1
calculating y**d % n
278537**1336577 % 989789 = 50
got char 2
decrypted 012

"""
import random


def gcd(x, y):
    """
    Euclid's algorithm for finding the greatest common divisor
    :param x:
    :param y:
    :return:
    """
    while y != 0:
        x, y = y, x % y
    return x


def is_prime(x):
    if x < 2 or x % 2 == 0:
        return False
    if x == 2:
        return True
    for n in range(3, int(x**0.5) + 2, 2):
        if x % n == 0:
            return False
    return True


def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm to find multiplicative inverse
    find the number d, such that
    e^-1 === d % phi
    Example:
        multiplicative_inverse(20, 97) -> 34
        multiplicative_inverse(34, 97) -> 20
    :param e:
    :param phi:
    :return: d
    """
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    assert temp_phi == 1
    return d


def find_e(phi):
    # choose e such that e and phi(n) are coprimes (their gcd = 1)
    g = 0
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    assert e
    return e


def generate_keypair(p, q):
    if not is_prime(p):
        raise ValueError("p should be prime")
    if not is_prime(q):
        raise ValueError("q should be prime")
    n = p * q
    # find totient of n: phi(n)
    phi = (p - 1) * (q - 1)

    if p*q > 10000:
        e = 65537
    else:
        e = find_e(phi)
    print("e", e, "phi", phi)
    # generate private key
    d = multiplicative_inverse(e, phi) + phi
    public_key = e, n
    private_key = d, n
    return public_key, private_key


def encrypt(public_key, plain):
    e, n = public_key
    ords = [ord(a) for a in plain]
    print("ords", ords)
    cipher = []
    for x in ords:
        print("calculating x**e % n")
        #y = (x ** e) % n
        y = pow(x, e, n)
        print("{}**{} % {} = {}".format(x, e, n, y))
        cipher.append(y)
    return cipher


def decrypt(private_key, cipher):
    d, n = private_key
    plain = []
    for y in cipher:
        print("calculating y**d % n")
        #x = (y ** d) % n # takes 22 seconds
        x = pow(y, d, n)  # equivalent to y**d%n
        print("{}**{} % {} = {}".format(y, d, n, x))
        char = chr(x)
        print("got char", char)
        plain.append(char)
    return ''.join(plain)


# min pair of primes to work
p, q = 11, 7
# p, q = 557, 1777

print("p", p, ", q", q, ", n=p*q", p*q)
public_key, private_key = generate_keypair(p, q)
print("public (e, n){}".format(public_key))
print("private(d, n){}".format(private_key))
msg = "012"
print("original msg", msg)
encrypted = encrypt(public_key, msg)
print("encrypted", encrypted)
decrypted = decrypt(private_key, encrypted)
print("decrypted", decrypted)
