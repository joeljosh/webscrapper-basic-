from urllib.request import urlopen
import urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = input('Enter URL ')
print('Retrieving', url)

uh = urlopen(url, context=ctx)
data=uh.read().decode()

info=json.loads(data)

print('Retrieved', len(data), 'characters')


###REPLACE CODE BELOW WITH DESIRED CODEBLOCK###
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
