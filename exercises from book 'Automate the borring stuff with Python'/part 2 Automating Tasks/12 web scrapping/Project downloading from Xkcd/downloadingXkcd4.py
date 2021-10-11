import bs4, requests, os
mainUrl = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
while not mainUrl.endswith('#'):
    print('Downloading page %s' % mainUrl)
    res = requests.get(mainUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    imgElem = soup.select('#comic img')
    if imgElem == []:
        print('cant find image')
    else:
        imgLink = 'https:' + imgElem[0].get('src')
        print('downloading image %s' % imgLink)
        res = requests.get(imgLink)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(imgLink)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    mainUrl = 'https://xkcd.com' + prevLink.get('href')

print('done')