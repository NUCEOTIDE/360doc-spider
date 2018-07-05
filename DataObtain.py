import os
import DataPorcess
from selenium import webdriver  # 导入Selenium的webdriver


#  默认header一般不做修改如要修改直接改以下文本
#  默认url按照每次访问从rulList中取得的值修改
url='https://www.baidu.com'
driver=None
years=''
response=''
order=1
moduleAddress=os.path.abspath(__file__)
urlFolder=moduleAddress[:moduleAddress.find(r'\DataObtain.py')]+"\\"+"urlList"+"\\"
# 本机地址 r"C:\Users\user\Desktop\FTC\2018个人项目\数据爬虫\360doc-spider\urlList"+"\\"



def request_initial(new_url):
	global url, driver
	try:
		url=new_url  # 目标url地址
		driver=webdriver.Chrome()  # 初始化浏览器，使用Chrome测试。完成时使用PhantomJS提高速度
	except ValueError:
		print('错误的url，或者url不存在')
	finally:
		return


def requests():
	global url,driver,years,response,order
	try:
		driver.get(url)
		response=driver.page_source
		print('{}-{} data obtaining complete'.format(years,order))
		order+=1
	finally:
		driver.close()
		return response


def dataObtain(new_years):
	global years,response
	# 从位于此地址的urlFolder中查找相关年份的list
	# print(urlFolder)
	urlFile=open(urlFolder+"urlList"+str(new_years)+".txt")  # 文件命名方式‘urlList’+年份，txt格式
	years=new_years
	targetDir=moduleAddress[:moduleAddress.find(r'\DataObtain.py')]+'\\{}'.format(years)
	# 本机地址 r'C:\Users\user\Desktop\FTC\2018个人项目\数据爬虫\360doc-spider\{}'.format(years)
	# 如果子目录尚不存在则创建一个
	if not os.path.exists(targetDir):
		os.mkdir(targetDir)
		print('Successfully created directory', targetDir)
	for urlLine in urlFile.readlines():  # 如果文件读取完毕，结束循环
		new_url=urlLine  # 从urlList文件中一行行读取目标网址
		request_initial(new_url)
		print(targetDir)
		DataPorcess.dataProcess(requests(),targetDir)
	print('data obtaining&processing completed')


print(dataObtain('2013'))  # 测试代码
