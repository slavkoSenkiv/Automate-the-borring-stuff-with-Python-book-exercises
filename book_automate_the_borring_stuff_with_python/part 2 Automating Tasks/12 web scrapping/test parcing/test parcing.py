import bs4, requests
res = requests.get('https://www.weather.gov/')
print(res.raise_for_status())
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(1, type(noStarchSoup))

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(2, type(exampleSoup))