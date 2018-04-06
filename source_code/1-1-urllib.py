import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# if has Chinese, apply decode()
html = urllib.request.urlopen("http://www.ieee.org/index.html").read().decode('utf-8')
print(html)


import res
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])


res = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)    # re.DOTALL if multi line
print("\nPage paragraph is: ", res[0])
# Page paragraph is:


res = re.findall(r'href="(.*?)"', html)
print("\nAll links: ", res)
# All links:  ['https://morvanzhou.github.io/static/img/description/tab_icon.png', 'https://morvanzhou.github.io/', 'https://morvanzhou.github.io/tutorials/scraping']