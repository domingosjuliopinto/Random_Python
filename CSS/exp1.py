J_C_Dict = {
        "a" : 0 ,
        "b" : 1 ,
        "c" : 2 ,
        "d" : 3 ,
        "e" : 4 ,
        "f" : 5 ,
        "g" : 6 ,
        "h" : 7 ,
        "i" : 8 ,
        "j" : 9 ,
        "k" : 10 ,
        "l" : 11 ,
        "m" : 12 ,
        "n" : 13 ,
        "o" : 14 ,
        "p" : 15 ,
        "q" : 16 ,
        "r" : 17 ,
        "s" : 18 ,
        "t" : 19 ,
        "u" : 20 ,
        "v" : 21 ,
        "w" : 22 ,
        "x" : 23 ,
        "y" : 24 ,
        "z" : 25 ,
    }

key_list = list(J_C_Dict.keys())
val_list = list(J_C_Dict.values())

def caesar_cipher():
    t = input("Enter Text String :\n")
    t = remove_space(t)
    k=int(input("Enter Key (integer) :\n"))
    choice = input("Enter\n0-To Encrypt\n1-To Decrypt\nOther characters-To Exit\nYour Choice : ")
    if(choice == '0'):
        encrypt_caesar(t,k)
    elif(choice == '1'):
        decrypt_caesar(t,k)
    else:
        pass

def encrypt_caesar(text,key):
    textl = text.lower()
    encrypted = ""
    for i in range(len(textl)):
        char = textl[i]
        formula = (int(J_C_Dict[char])+ key)%26
        position = val_list.index(formula)
        encrypted +=(key_list[position]+" ")
    print(encrypted.upper())

def decrypt_caesar(text,key):
    textl = text.lower()
    decrypted = ""
    for i in range(len(textl)):
        char = textl[i]
        check = int(J_C_Dict[char])- key
        if(check<0):
            check+=26
        else:
            pass
        formula = check % 26
        position = val_list.index(formula)
        decrypted +=(key_list[position]+" ")
    print(decrypted)

def remove_space(string):
    return string.replace(" ", "")

def encrypt_railfence(text,key):
    text_mod = remove_space(text)
    rail = [['\n' for i in range(len(text_mod))]for j in range(key)]
    direction = False
    row, col = 0, 0
     
    for i in range(len(text_mod)):
         
        if (row == 0) or (row == key - 1):
            direction = not direction
         
        rail[row][col] = text_mod[i]
        col += 1
         
        if direction:
            row += 1
        else:
            row -= 1

    encrypt = []
    
    for i in range(key):
        for j in range(len(text_mod)):
            if rail[i][j] != '\n':
                encrypt.append(rail[i][j])
        encrypt.append(" ")

    return("" . join(encrypt))

def decrypt_railfence(cipher, key):
    cipher_mod = remove_space(cipher)
    rail = [['\n' for i in range(len(cipher_mod))] for j in range(key)] 
    direction = False
    row, col = 0, 0
     
    for i in range(len(cipher_mod)):
        if (row == 0) or (row == key - 1):
            direction = not direction
    
        rail[row][col] = '*'
        col += 1
         
        if direction:
            row += 1
        else:
            row -= 1

    i=0
    for row in range(key):
        for column in range(len(cipher_mod)):
            if rail[row][column] == '*':
                rail[row][column]=cipher_mod[i]
                i=i+1
            if i == len(cipher_mod):
                break
            else:
                continue
    
    result = []
    row, col = 0, 0
    for i in range(len(cipher_mod)):
         
        if row == 0:
            direction = True
        if row == key-1:
            direction = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
            
        if direction:
            row += 1
        else:
            row -= 1
    return("".join(result))

def railfence():
    t = input("Enter Text String :\n")
    k=int(input("Enter Key (integer) :\n"))
    choice = input("Enter\n0-To Encrypt\n1-To Decrypt\nOther characters-To Exit\nYour Choice : ")
    if(choice == '0'):
        print(encrypt_railfence(t,k))
    elif(choice == '1'):
        print(decrypt_railfence(t,k))
    else:
        pass


def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
def locindex(c): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():  #Encryption
    msg=str(input("Enter text : "))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("Cipher Text:",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
def decrypt():  #decryption
    msg=str(input("Enter Cipher Text : "))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("Plain Text : ",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        

def playfair():
    key=input("Enter key : ")
    key=key.replace(" ", "")
    key=key.upper()
    result=list()
    for c in key: #storing key
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91): #storing other character
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    for i in range(0,5): #making matrix
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1

    print(my_matrix)
    choice=int(input("\n0 for Encryption \n1 for Decryption: \nOther for Exit\nYour Choice : "))
    if choice==0:
        encrypt()
    elif choice==1:
        decrypt()
    else:
        pass

my_matrix=matrix(5,5,0) #initialize matrix

cipher = int(input("Enter\n0-For Caesar Cipher\n1-For PlayFair Cipher\n2-For Railfence Cipher\nOther characters-To Exit\nYour Choice : "))
if(cipher == 0):
    caesar_cipher()
elif(cipher == 1):
    playfair()
elif(cipher == 2):
    railfence()
else:
    pass
