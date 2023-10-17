# Armstrong number
num = input("Enter Number \n")
str = str(num)
pow = len(str)
sum=0
temp = num
while temp>0:
    digit = temp % 10
    sum = sum + (digit ** pow)
    temp = temp / 10
if num == sum:
    print(str + " is armstrong number")
else:
    print(str + " is not armstrong number")
