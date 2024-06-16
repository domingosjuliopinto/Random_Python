import nltk

#nltk.download('all')
sentence = "So goodbye yellow brick road. Where the dogs of society howl. You can't plant me in your penthouse. I'm going back to my plough."

#word tokenize
tokens = nltk.word_tokenize(sentence)
print(tokens)

print("")
#sentence tokenize
sentoken = nltk.sent_tokenize(sentence)
print(sentoken)

print("")
# stemming using PorterStemmer  
pStemmer = nltk.PorterStemmer()  
  
# selecting some words to be stemmed

list_of_words = ["crying"]  
print("Enter 4 words to stem")
for i in range(4):
    x = input()
    list_of_words.append(x)
  
for words in list_of_words:  
    print(words + ": " + pStemmer.stem(words))

#Lemmatizer
lemmatizer = nltk.WordNetLemmatizer()
print(" ")
print("after lemmatizer, crying :", lemmatizer.lemmatize("crying"))

#stopword removal
from nltk.corpus import stopwords
example_sent = "India is my country"
stop_words = set(stopwords.words('english'))
word_tokens = nltk.word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  
filtered_sentence = []
  
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print("")
print("after stopword removal ", filtered_sentence)

#filteration
sentence_mix ="कौन हे  class coordinator ?"
print(" ")
print('After Filtration: ' + ''.join(list(filter(lambda x: ord(x) < 123, sentence_mix))))

#script-validator
import string
text = "We will meet tomorrow @ 9am ."
text_p = "".join([char for char in text if char not in string.punctuation])
print(" ")
print(text_p)
