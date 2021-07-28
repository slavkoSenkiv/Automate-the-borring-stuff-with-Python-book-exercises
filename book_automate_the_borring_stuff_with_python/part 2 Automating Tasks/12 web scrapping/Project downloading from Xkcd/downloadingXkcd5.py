import requests, bs4, os

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('cant find image')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('downloading a page %s ' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    previousLink = soup.select('a[rel = "prev"]')[0]
    url = 'https://xkcd.com/' + previousLink.get('href')

print('done')