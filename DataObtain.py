import urllib.request
import urllib.response
import sys

#  默认header一般不做修改如要修改直接改以下文本
header={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		              'Chrome/67.0.3396.99 Safari/537.36 '
	}
#  默认url按照每次访问从rulList中取得的值修改
url='https://www.baidu.com'


def request_initial(new_url):
	try:
		global url
		url=new_url  # 目标url地址
	except ValueError:
		print('错误的url，或者url不存在')
	finally:
		return


def dataObtain(years):
	global url, header
	urlFile=open("urlList"+str(years)+".txt")  # 文件命名方式‘urlList’+年份，txt格式
	while True:
		new_url=urlFile.readline()  # 从urlList文件中一行行读取目标网址
		if new_url==0:
			break  # 如果文件读取完毕，结束循环
		request_initial(new_url)
		requests()
		return url,header
	print('data obtaining completed')


def requests():
	global url,header
	request=urllib.request.Request(url=url, headers=header)  # 像目标url地址发送response请求，返回一个response对象
	response=urllib.request.urlopen(request).read()
	type=sys.getfilesystemencoding()  # 设置爬出内容的编码
	response=response.decode(type)
	#  file = open("c.txt", 'w', 10000)
	#  file.write(str(response))
	#  file.close()
	#  print(response)  # r.text是http response的网页HTML
	return response


#  print(dataObtain(2013))  测试代码
