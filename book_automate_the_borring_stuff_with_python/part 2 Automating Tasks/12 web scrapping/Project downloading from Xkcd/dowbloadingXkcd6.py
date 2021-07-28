import bs4, requests, os
from pathlib import Path

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('downloading a page %s' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imageElem = soup.select('#comic img')
    if imageElem == []:
        print('there is no image')
    else:
        comicUrl = 'https:' + imageElem[0].get('src')

        print('downloading a file %s' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(1000):
            imageFile.write(chunk)

        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com/' + prevLink.get('href')

print('done')
