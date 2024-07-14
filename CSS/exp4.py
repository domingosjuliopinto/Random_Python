def create_public_key(p,g, str):
    X=int(input("\nEnter private key "+str+" : "))
    while(X>=p):
        print("Enter a valid private key.")
        X=int(input("\nEnter private key "+str+" : "))
    return (g**X)%p,X

def sender(Yb,Xa,p):
    return (Yb**Xa)%p

def receiver(Ya,Xb,p):
    return (Ya**Xb)%p

def gcd(p,q):
    while (q!=0):
        p,q=q,p%q
    return p

def prim_roots(p):
    roots=[]
    coprime_nums=set(num for num in range (1,p) if gcd(num,p)==1)
    for g in range(1, p):
        actual_set=set(pow(g,powers)%p for powers in range (1,p))
        if (coprime_nums==actual_set):
            roots.append(g)
    return roots

p=int(input("Enter p: "))
g=prim_roots(p)
print("Primitive roots of p:\n",g)
print("\n*****The first value from the list will be used as g*****\n Therefore g = ",g[0])
Ya,Xa=create_public_key(p,g[0],"Xa")
Yb,Xb=create_public_key(p,g[0],"Xb")
print("\nShared key(sender side):",sender(Yb,Xa,p))
print("Shared key(receiver side):",receiver(Ya,Xb,p))
