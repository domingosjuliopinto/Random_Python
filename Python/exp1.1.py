# Greatest of 3 numbers
n1=input("Enter 1st no \n")
n2=input("Enter 2nd no \n")
n3=input("Enter 3rd no \n")
g=n1 if n1>n2 else n2
g=g if g>n3 else n3
print(str(g) + " Is the Greatest of the 3 numbers")
