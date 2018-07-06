import os
import DataProcess
from selenium import webdriver  # 导入Selenium的webdriver


url='https://www.baidu.com'  # 默认url按照每次访问从rulList中取得的值修改
driver=None  # 初始driver,实际根据驱动可在Chrome与phantomJS以及其它支持浏览器间切换
years=''  # 初始年份变量
response=''  # 初始页面信息
order=1
moduleAddress=os.path.abspath(__file__)
urlFolder=moduleAddress[:moduleAddress.find(r'\DataObtain.py')]+"\\"+"urlList"+"\\"  # 默认链接列表文件夹地址
# 本机地址 r"C:\Users\user\Desktop\FTC\2018个人项目\数据爬虫\360doc-spider\urlList"+"\\"


def dataObtain(new_years):
	'''通过访问位于项目文件夹r'360doc-spider\\urlList\\'内部的相关年份的链接列表。
	依次访问网页完成下载，把原始数据保存通过调用DataProcess处理
	保存至r'360doc-spider\\rawFile\\xxxx\\'中的txt文件中'''

	global years,response
	years=new_years
	try:
		# 从位于此地址的urlFolder中查找相关年份的list
		urlFile=open(urlFolder+"urlList"+str(years)+".txt")   # 文件命名方式‘urlList’+年份，txt格式
		targetDir_text=moduleAddress[:moduleAddress.find(r'\DataObtain.py')]+'\\'+'rawFile'+'\\{}'.format(years)
		# 本机地址 r'C:\Users\user\Desktop\FTC\2018个人项目\数据爬虫\360doc-spider\rawFile\{}'.format(years)
		targetDir_pics=moduleAddress[:moduleAddress.find(r'\DataObtain.py')]+'\\'+'rawPics'+'\\{}'.format(years)
		# 本机地址 r'C:\Users\user\Desktop\FTC\2018个人项目\数据爬虫\360doc-spider\rawPics\{}'.format(years)
		# 如果子目录尚不存在则创建一个
		if not os.path.exists(os.path.dirname(targetDir_text)):
			print('指定文件保存路径不存在，将创建指定路径')
			os.mkdir(os.path.dirname(targetDir_text))
			print('成功创建路径',os.path.dirname(targetDir_text))
		if not os.path.exists(os.path.dirname(targetDir_pics)):
			print('指定图片保存路径不存在，将创建指定路径')
			os.mkdir(os.path.dirname(targetDir_pics))
			print('成功创建路径',os.path.dirname(targetDir_pics))
		if not os.path.exists(targetDir_text):
			print('指定文件年份路径不存在，将创建指定路径')
			os.mkdir(targetDir_text)
			print('成功创建路径',targetDir_text)
		if not os.path.exists(targetDir_pics):
			print('指定图片年份路径不存在，将创建指定路径')
			os.mkdir(targetDir_pics)
			print('成功创建路径', targetDir_pics)
	except FileNotFoundError:
		print('无法创建路径')
	for urlLine in urlFile.readlines():  # 如果文件读取完毕，结束循环
		new_url=urlLine  # 从urlList文件中一行行读取目标网址
		request_initial(new_url)
		DataProcess.dataProcess(requests(),targetDir_text,targetDir_pics)
	print('数据获取并处理成功')


def request_initial(new_url):
	'''初始化浏览器'''
	global url, driver
	try:
		url=new_url  # 目标url地址
		driver=webdriver.Chrome()  # 初始化浏览器，使用Chrome测试。完成时使用PhantomJS提高速度
	except ValueError:
		print('错误的url，或者url不存在 ')
	finally:
		return


def requests():
	'''访问目标页面'''
	global url,driver,years,response,order
	try:
		driver.get(url)
		response=driver.page_source
		print('{}-{} 数据获取成功 '.format(years,order))
		order+=1
	except TimeoutError:
		pass
	finally:
		driver.close()
		return response


print(dataObtain('2013'))  # 测试代码
