#sentence = "Goodbye Yellow Brick Road"
#str1 = "he has not poor skills"
str1 = "his skills are not that poor"
#s1 = "play"
#s1 = "of"
#s1 = "amazing"

"""
t = len(sentence)
print(t)
"""
"""
k = len(sentence.replace(" ",""))
print(k)
"""

"""
if len(sentence) < 2:
    print('')
else:
    print(sentence[0:2] + sentence[-2:])
"""
"""
char = sentence[0]
sentence = sentence.replace(char, '$')
print(char + sentence[1:])
"""
"""
new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]

print(new_s1 + ' ' + new_s2)
"""
"""
length = len(s1)

if length > 2:
    if s1[-3:] == 'ing':
        s1 += 'ly'
    else:
        s1 += 'ing'

print(s1)
"""

pos_not = str1.find('not')
pos_poor = str1.find('poor')

print("first occurence of not ",pos_not)
print("first occurence of poor ",pos_poor)

if pos_poor > pos_not and pos_not>0 and pos_poor>0:
    str1 = str1.replace(str1[pos_not:(pos_poor+4)], 'good')
    print (str1)
else:
    print (str1)

"""
d = sentence.split(" ")
n = len(d)
g = 0
for i in range(n):
    t = len(d[i])
    if t > g:
        g = t
print(g)
"""
"""
print(s1.replace(s1[-1],""))
"""
"""
ns = s1[-1]+s1[1:-1]+s1[0]
print(ns)
"""
"""
t = len(s1)
r = "" 
for i in range(len(s1)):
    if i % 2 == 0:
        r = r + s1[i]
print(r)
"""
"""
str = "Betty Botter bought a bit of butter. But, she said, the butter's bitter. If I put it in my batter, it will make my batter bitter. But, a bit of better butter will make my batter better"
counts = dict()
words = str.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
"""

"""
a = input()
print(a.upper())
print(a.lower())
"""
"""
l = input()
l = l.replace(" ","")
d = l.split(",")
d.sort()
for words in d:
    print(words)
"""
"""
l = input()
print("<i>"+l+"</i>")
print("<b>"+l+"</b>")
"""
