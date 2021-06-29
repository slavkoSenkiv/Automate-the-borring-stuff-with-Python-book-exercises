
import requests, bs4, os

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('reading %s page' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imgEl = soup.select('#comic img')
    if imgEl == []:
        print('cant find element')
    else:
        imgUrl = 'https:' + imgEl[0].get('src')
        print('downloading an image %s' % imgUrl)
        imgFile = open(os.path.join('xkcd', os.path.basename(imgUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()

    prevUrl = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com/' + prevUrl.get('href')

print('Done')
