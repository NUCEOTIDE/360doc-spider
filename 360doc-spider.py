import urllib.request
import urllib.response

header={
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
url='https://www.baidu.com' #像目标url地址发送response请求，返回一个response对象

request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request).read()
a=urllib.request.urlopen(url)
print(response) #r.text是http response的网页HTML