# coding = utf-8
import urllib.request
import ssl
 
ssl._create_default_https_context = ssl._create_unverified_context
response = urllib.request.urlopen('https://www.douban.com/')
print(response.read().decode('utf-8'))