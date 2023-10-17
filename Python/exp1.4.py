# program to count the occurrences of a word in a given sentence
sen=input("Enter Sentence within two double apostrophe\n")
word = str(input("Enter Word within two double apostrophe \n"))
count=0
lst=[]
lst=(sen.split(" "))
for i in range(len(lst)):
    if (word==lst[i]):
        count=count+1
print("Count of word is " + str(count))

