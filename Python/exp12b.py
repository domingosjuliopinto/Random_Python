import urllib.parse
url='https://en.wikipedia.org/wiki/Pythagorean_theorem'
tpl=urllib.parse.urlparse(url)
print(tpl)
print(tpl.scheme)
