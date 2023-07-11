import requests
import json
url = "https://aws.random.cat/meow"
response = requests.get(url)

print('STATUS:  ', response.status_code)
print('RESPONSE:', response.text)  # json

data = response.json()  # equivale a: json.loads(response.text)
print('DICT:    ', data)

url = data['file']
print('URL:     ', url)
print()

from IPython.display import Image  # https://ipython.org/ipython-doc/dev/api/generated/IPython.display.html
Image(url, width=300, height=300)