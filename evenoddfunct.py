def evenodd(num):
    if (num % 2) == 0:
        print("{0} is Even number".format(num))  
    else:
        print("{0} is Odd number".format(num))

num = int(input("Enter a number: "))
evenodd(num)
