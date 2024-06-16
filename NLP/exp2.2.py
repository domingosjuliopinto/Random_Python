import re

#removal of url
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'',text)

text = input("Enter a string with a link and html tag: ")
text1 = remove_urls(text)
print("After removal of url")
print(text1)
print("")
#removal of html tags
def remove_tag(text):
    text=' '.join(text)
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'',text)

text2 = remove_tag(text1.split()) 
print("After removal of html tags")
print(text2)
print("")

#removal of lowercase
remove_lower = lambda text: re.sub('[a-z]','',text)
result = remove_lower(text2)
print("After removal of lowercase")
print(result)
