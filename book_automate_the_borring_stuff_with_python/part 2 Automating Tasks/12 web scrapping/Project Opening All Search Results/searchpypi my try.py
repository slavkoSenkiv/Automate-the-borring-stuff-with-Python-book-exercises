import requests, webbrowser, bs4

searchTerm = input('enter your search term: ')
print('Searching')
res = requests.get('https://pypi.org/search/?q=' + ' '.join(searchTerm))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')
numLinks = min(5, len(linkElems))
for i in range(numLinks):
    link = 'https://pypi.org' + linkElems[i].get('href')
    webbrowser.open(link)