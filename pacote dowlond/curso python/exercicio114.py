import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('Internet fora do ar!')
else:
    print('Internet OK!')
    print(site.read())