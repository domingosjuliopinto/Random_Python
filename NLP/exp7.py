import nltk
text = str(input("Enter the sentence to get the tree: "))
tokens = nltk.word_tokenize(text)
print(tokens)
tag = nltk.pos_tag(tokens)
print(tag)
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp  =nltk.RegexpParser(grammar)
result = cp.parse(tag)
print(result)
for subtree in result.subtrees(filter=lambda t: t.label() == 'NP'):
    print(subtree)
result.draw() 
print("Graph closed")
