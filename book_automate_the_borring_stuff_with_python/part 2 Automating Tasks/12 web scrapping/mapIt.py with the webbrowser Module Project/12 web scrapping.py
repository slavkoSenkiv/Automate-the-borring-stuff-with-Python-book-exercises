

# Downloading a Web Page with the requests.get() Function
"""
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])"""

# Checking for Errors
"""
import requests
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    print(res.raise_for_status())
except Exception as exc:
    print('there was a problem: %s ' % (exc))"""

# Saving Downloaded Files to the Hard Drive
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.raise_for_status())
playFile = open('romeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    print(playFile.write(chunk))

playFile.close()

