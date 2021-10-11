import webbrowser, bs4, requests

searchTerm = input('enter your search:...')
url = 'https://pypi.org/search/?q=' + searchTerm
resultPage = requests.get(url)
resultPage.raise_for_status()
soup = bs4.BeautifulSoup(resultPage.text, 'html.parser')
linksElems = soup.select('.package-snippet')
numLinks = min(5, len(linksElems))
for i in range(numLinks):
    link = 'https://pypi.org' + linksElems[i].get('href')
    webbrowser.open(link)