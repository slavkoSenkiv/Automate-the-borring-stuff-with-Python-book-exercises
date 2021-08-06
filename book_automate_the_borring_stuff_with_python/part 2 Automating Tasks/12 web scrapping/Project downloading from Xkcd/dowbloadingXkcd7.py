import requests, bs4, os

url = 'https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print(f'downloading page {url}')
    page = requests.get(url)
    page.raise_for_status()
    page_soup = bs4.BeautifulSoup(page.text, 'html.parser')
    img_element = page_soup.select('#comic img')
    if not img_element:
        print('cant find image')
    else:
        img_url = 'https:' + img_element[0].get('src')
        print(f'downloading image {img_url}')
        image = requests.get(img_url)
        image.raise_for_status()
        image_file = open(os.path.join('xkcd', os.path.basename(img_url)), 'wb')
        for chunk in image.iter_content():
            image_file.write(chunk)
        image_file.close()
    previous_link = page_soup.select('a[rel="prev"]')
    url = 'https://xkcd.com/' + previous_link[0].get('href')
print('done')



