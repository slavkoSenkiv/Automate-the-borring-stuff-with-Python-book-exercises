

# Downloading a Web Page with the requests.get() Function
"""
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])"""

# Checking for Errors
"""
import requests
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    print(res.raise_for_status())
except Exception as exc:
    print('there was a problem: %s ' % (exc))"""

# Saving Downloaded Files to the Hard Drive
"""import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.raise_for_status())
playFile = open('romeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    print(playFile.write(chunk))

playFile.close()"""

# Parsing HTML with the bs4 Module


"""
import bs4, requests
res = requests.get('https://www.weather.gov/')
print(1.1, res.raise_for_status())
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(1.2, type(noStarchSoup))"""

"""exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

elems = exampleSoup.select('#author')
print(1, type(elems))  #  elems is a list of tag objects
print(2, len(elems))
print(3, type(elems[0]))
print(4, str(elems[0]))  # the tag object as a string
print(5, elems[0].getText())
print(6, elems[0].attrs)
print('_________________________\n')

pElems = exampleSoup.select('p')
print(1, str(pElems[0]))
print(2, pElems[0].getText())
print(3, str(pElems[1]))
print(4, pElems[1].getText())
print(5, str(pElems[1]))
print(6, pElems[1].getText())"""

"""
import requests, bs4

htmlFile = open('example.html', 'r')
htmlBsObject = bs4.BeautifulSoup(htmlFile.read(), 'html.parser')
pElems = htmlBsObject.select('p')

print(type(pElems))
print(pElems)
print(type(pElems[2]))
print(len(pElems))
print()

print(pElems[0])
print(pElems[1])
print(pElems[2])
print()

print(pElems[0].getText())
print(pElems[1].getText())
print(pElems[2].getText())
print()

print(pElems[0].attrs)
print(pElems[1].attrs)
print(pElems[2].attrs)
print()
"""

"""
# Getting Data from an Element’s Attributes
import bs4
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_noneexistent_addr') == None)
print(spanElem.attrs)"""


