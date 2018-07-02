import urllib.request
import urllib.response
import sys

header={
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/67.0.3396.99 Safari/537.36 '
}
url='http://www.360doc.com/content/17/0602/13/19119980_659271925.shtml' #像目标url地址发送response请求，返回一个response对象

request = urllib.request.Request(url=url,headers=header)
response = urllib.request.urlopen(request).read()
a=urllib.request.urlopen(url)
type = sys.getfilesystemencoding()
#设置爬出内容的编码
response = response.decode(type)
file = open("c。txt",'w',10000)
file.write(str(response))
file.close()
print(response)#r.text是http response的网页HTML