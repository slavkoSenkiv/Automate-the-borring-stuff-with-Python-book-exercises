import os, bs4, requests

os.makedirs('testFolder2', exist_ok=True)
url = 'https://xkcd.com/'

while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imgElem = soup.select('#comic img')
    if imgElem == []:
        print('cant find this element')
    else:
        imageUrl = 'https:' + imgElem[0].get('src')
        print('Downloading image %s' % imageUrl)
        imgRes = requests.get(imageUrl)
        imgRes.raise_for_status()
        imageFile = open(os.path.join('testFolder2', os.path.basename(imageUrl)), 'wb')
        for chunk in imageRes.iter_content(100000):
            imageFile.write(chunk)

        imageFile.close()

    prevElem = soup.select('p[rel = "prev"]')[0]
    url = 'https://xkcd.com' + prevElem.get('href')

print('Done')

