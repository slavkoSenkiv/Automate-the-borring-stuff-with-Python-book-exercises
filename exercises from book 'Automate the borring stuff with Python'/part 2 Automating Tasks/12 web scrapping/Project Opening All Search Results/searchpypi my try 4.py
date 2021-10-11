import webbrowser, bs4, requests
search = input('enter your search:...')
res = requests.get('https://pypi.org/search/?q=' + search)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElems = soup.select('.package-snippet')
numLinks = min(5, len(linkElems))
for i in range(numLinks):
    webbrowser.open('https://pypi.org' + linkElems[i].get('href'))