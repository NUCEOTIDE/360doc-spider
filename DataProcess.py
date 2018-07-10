from bs4 import BeautifulSoup
from selenium import webdriver


isObtained=False
pageSource_soup=None
contentString = '@'  # 特殊标识文件以@形式开启
file=None
years=''
header={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
	(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


def dataProcess(pageSource,fileAddress,new_years):
	'''处理保存在字符串中的原始数据，输出数据保存在txt格式文件中'''
	if pageSource==-1:
		return -1
	global isObtained,pageSource_soup,years
	years=new_years
	pageSource_soup=BeautifulSoup(pageSource,'lxml')  # 将获取的网页信息保存成BeautifulSoup对象
	find_text(fileAddress)
	find_picture(fileAddress)
	return 1


def find_picture(picAddress):
	global isObtained,years

	# 对图片信息进行获取
	pictures = pageSource_soup.find_all('table')[0]
	try:
		print('开始请求图片地址')
		count=0
		for pic in pictures.find_all('img'):
			count+=1
			picName=pageSource_soup.find('h2').string+' No.'+str(count)
			print(pic.attrs['src'])
			driver=webdriver.Chrome()
			print('开始保存图片')
			# img.urlretrieve(img, picAddress + '\\' + picName)
			#feedback=urllib.request.urlopen(img).read()
			driver.get(pic.attrs['src'])
			feedback=driver.page_source
			f=open(picAddress+'\\'+picName, 'ab')
			f.write(feedback)
			f.close()
			print(picAddress+'\\'+picName,'图片保存成功！')
	except TimeoutError:
		print('请求超时，请检查网络连接')
	except TypeError:
		print('请求失败，未能下载图片')


def find_text(fileAddress):
	global isObtained,contentString

	# 对文字信息进行获取
	# 由于需求信息存在于网页的ta_name为table的内容下，专门搜索本内容
	table = pageSource_soup.find_all('table')[1]
	try:
		for line in table.find_all('td'):
			isObtained = True
			if line.get_text() == '同时发行':
				break
			else:
				contentString += line.get_text() + '~'
		if isObtained:
			print('目标内容已转移自字符串中')
		else:
			print('无法找到目标内容')
	except FileNotFoundError:
		print('无法找到文件')
	finally:
		fileName = pageSource_soup.find('h2').string  # 创建新文件
		file = open(fileAddress + "\\" + fileName + '.txt', mode='w', encoding='utf-8')
		file.write(contentString)  # 将结果写入文件
		file.close()  # 关闭文件
		print('{}\n 文件创建并写入成功'.format(fileName))
		contentString='@'
		isObtained=False
		return

