# program to demonstrate string datatype 
# with single Quotes  
String1 = 'Python should be easy'
print("String with the use of Single Quotes: \n")  
print(String1)
print("Length of the above string is "+ str(len(String1)))
print(String1.upper())
print(String1.lower())
print(String1.replace("should", "will"))
    
# with double Quotes  
String2 = "Who am We ?"
print("\nString with the use of Double Quotes:\n ")  
print(String2)  
print(type(String2)) 
     
# with triple Quotes  
String3 = '''Why do we live in this "world"?'''
print("\nString with the use of Triple Quotes: \n")  
print(String3)  
print(type(String3)) 

print ("String Concatenation = "+String2+String3)
  
# Quotes allows multiple lines  
String4 = '''Python  
            For  
            Coding'''
print("\nCreating a multiline String:")  
print(String4)  

String5 = 'peace'
print(String5*3)
print(String5.capitalize())
print(String5[2:])
print(String5[:3])
print(String5[2])
print(String5[0:4])
