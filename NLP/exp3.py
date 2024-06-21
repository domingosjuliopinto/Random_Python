import re
"""
#q1
def text_match_q1(text):
    patterns = '^a(b*)(.*)$'
    if re.search(patterns,text):
        return 'Found a match!'
    else:
        return('Not matched!')

text1 = input("Enter a string : ")
print(text_match_q1(text1))
"""
"""
#q2
def text_match_q2(text):
    patterns = '^a(b+)(.*)$'
    if re.search(patterns,text):
        return 'Found a match!'
    else:
        return('Not matched!')

text2 = input("Enter a string : ")
print(text_match_q2(text2))
"""
"""
#q3
def text_match_q3(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns,text):
        return 'Found a match!'
    else:
        return('Not matched!')

text3 = input("Enter a string : ")
print(text_match_q3(text3))
"""
"""
#q4
def text_match_q4(text):
    patterns = '[A-Z][a-z]+$'
    if re.search(patterns,text):
        return 'Found a match!'
    else:
        return('Not matched!')

text4 = input("Enter a string : ")
print(text_match_q4(text4))
"""
"""
#q5
def text_match_q5(text):
    patterns = '(.*)z(.*)+$'
    if re.search(patterns,text):
        return 'Found a match!'
    else:
        return('Not matched!')

text5 = input("Enter a string : ")
print(text_match_q5(text5))
"""
"""
#q6
def text_match_q6(text):
    patterns = '([^z])(.*)z(.*)([^z])+$'
    if re.search(patterns,text):
        return 'Found a match!'
    else:
        return('Not matched!')

text6 = input("Enter a string : ")
print(text_match_q6(text6))
"""
"""
#q7
def text_match_q7(text):
    patterns = '^[0-9A-Za-z_]+$'
    if re.search(patterns,text):
        return 'Found a match!'
    else:
        return('Not matched!')

text7 = input("Enter a string : ")
print(text_match_q7(text7))
"""
#q8

text8 = input("Enter the string with numbers: ")
result = re.findall('[0-9]+',text8)

def filternumber(n):
    if(len(n)<=3):
        return True
    else:
        return False

finalresult = list(filter(filternumber,result))
print(finalresult)

"""
#q9
patterns = [ 'fox', 'dog', 'horse' ]
text9 = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    if re.search(pattern,  text9):
        pos = text9.find(pattern)
        print(pattern + ' : found a match! at position ' + str(pos))
    else:
        print(pattern + ': Not matched!')
"""
"""
#q10
text10_1= 'This is'
text10_2= 'Experiment_3'
print(text10_1)
text10_1 =text10_1.replace (" ", "_")
print(text10_1)
print(text10_2)
text10_2 =text10_2.replace ("_", " ")
print(text10_2)
"""
"""
#q11
def text_match_q11(text):
    result = re.findall(r'[0-9]+',text)
    print(result)

text = input("Enter string with numbers : ")
text_match_q11(text)
"""
"""
#q12
text = """"""Yo, listen up here's a story
about a little guy
That lives in a blue world
and all day and all night
and everything he sees is just blue
Like him inside and outside""""""
list = re.findall(r"\ba\w+|\be\w+", text)
print(list)
"""
"""
#q13
street = input("The road name with Road : ")
print(re.sub('Road$', 'Rd.', street))
"""
"""
#q14
text14 = 'Sultan      Of      Swing'
print("Original string:",text14)
print("Without extra spaces:",re.sub(' +',' ',text14))
"""
"""
#q15
text15 = '**//Wakanda Forever// - 11. '
pattern = re.compile('[\W_]+')
print(pattern.sub('', text15))
"""
