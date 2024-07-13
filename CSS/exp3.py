import math

def key_gen(n,p,q):
    phi = (p-1)*(q-1)
    e = int(input("Enter a co-prime number of phi e:"))
    flage = False
    if flage == True:
        while flage == True:
            e = int(input("Not a prime number. Enter a prime number e : "))
            flage = prime(e)
    for i in range(phi):
        if (i*e)%phi == 1:
            d=i
            break
    return e,d

def rsa_encrypt(m,e,n):
    return (pow(m,e)%n)

def rsa_decrypt(m,d,n):
    return (pow(m,d)%n)

def prime(num):
    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break
    return flag

def RSA():
    p = int(input("Enter a prime number p : "))
    q = int(input("Enter a prime number q : "))
    flagp = prime(p)
    flagq = prime(q)
            
    # check if flag is True
    if flagp == True:
        while flagp == True:
            p = int(input("Not a prime number. Enter a prime number p : "))
            flagp = prime(p)
            
    if flagq == True:
        while flagq == True:
            q = int(input("Not a prime number. Enter a prime number q : "))
            flagq = prime(q)

    n=p*q
    e,d =key_gen(n,p,q)
    print(e)
    print(d)
    m = int(input("Enter the message(number) to encrypt : "))
    c = rsa_encrypt(m,e,n)
    p = rsa_decrypt(c,d,n)
    print("Public Key: (",n,e,")\nPrivate Key: (",n,d,")\n")
    print("Encrypted Text:",c)
    print("Decrypted Text:",p)

print("RSA Encryption Algorithm")
RSA()

