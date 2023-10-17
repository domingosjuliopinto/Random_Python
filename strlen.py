# Python code to demonstrate string length 
# using for loop
  
# Returns length of string
def findLen(str):
    counter = 0    
    for i in str:
        counter += 1
    return counter
  
  
str = "programmer"
print(findLen(str))

numbers = [1,2,3,4,5,6,7,8,9]

for x in numbers:
	print(x)
	
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
