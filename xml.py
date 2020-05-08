from urllib.request import urlopen
import urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Location ')
uh = urlopen(url, context=ctx)
data=uh.read()

print('Retrieved', len(data), 'characters')

data.decode()
tree=ET.fromstring(data)

###REPLACE CODE BELOW WITH DESIRED CODEBLOCK###

comments=tree.findall('comments/comment')
print('count:', len(comments))

sum=0

for comment in comments:
    sum=sum+int(comment.find('count').text)

print(sum)