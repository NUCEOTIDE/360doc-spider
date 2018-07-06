import urllib.request
import urllib.parse

url='http://userimage7.360doc.com/16/0119/15/27905781_201601191559020830761472.jpg'
header={
    'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}   #头部信息
request=urllib.request.Request(url,headers=header)
reponse=urllib.request.urlopen(request).read()

fh=open("./baidu.html","wb")    #写入文件中
fh.write(reponse)
fh.close()