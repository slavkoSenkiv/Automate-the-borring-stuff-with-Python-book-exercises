import requests, webbrowser, bs4

searchTerm = input('enter your searchTerm:..')
webbrowser.open('https://pypi.org/search/?q=' + searchTerm)
page = requests.get('https://pypi.org/search/?q=' + searchTerm)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.text, 'html.parser')
itemElems = soup.select('.package-snippet')
numLinks = min(5, len(itemElems))
for i in range(numLinks):
    packageUrl = 'https://pypi.org' + itemElems[i].get('href')
    webbrowser.open(packageUrl)



