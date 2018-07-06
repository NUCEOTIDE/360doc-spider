from bs4 import BeautifulSoup
from selenium import webdriver  # 导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  # 导入Keys
import time

url='http://www.360doc.com/userhome/27905781'
driver=None
alterDriver=None


def listObtain():
	'''通过模拟浏览器进行访问，获得目标邮票集的链接列表'''

	request_initial()
	templistFile=open('tempoRawList_info','w')
	templistFile.write(requests())
	pageSource=dynamicRequests()
	dataProcess(pageSource)


def request_initial():
	'''初始化浏览器'''

	global driver,alterDriver
	try:
		options = webdriver.ChromeOptions()
		options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
		driver = webdriver.Chrome(chrome_options=options)  # 指定使用的浏览器，初始化webdriver
		alterDriver = webdriver.PhantomJS()
	except ValueError:
		pass


def requests():
	'''访问目标页面'''

	global driver,alterDriver
	try:
		request_initial()
		alterDriver.get(url)  # 请求网页地址
	except ValueError:
		print('错误的url，或者url不存在 invalid or not exiting url')
	finally:
		return driver.page_source


def dynamicRequests():
	'''通过动态请求完成对页面上所有目标网址的下载'''

	try:
		time.sleep(3)
		alterDriver.find_element_by_xpath('//*[@id="treelist_652_switch"]').click()
		# 看看"馆藏分类"关键字是否在网页title中，如果在则继续，如果不在，程序跳出。
		print('关键字查找成功，程序继续')
		tempLevel=alterDriver.find_element_by_xpath('//*[@id="treelist_653_a"]')
		tempLevel.click()
		print(tempLevel)
	except webdriver.common.exceptions.NoSuchElementException:
		print('无法找到该元素')
	finally:
		return driver.page_source


def dataProcess(pageSource):
	'''对下载数据进行处理，方便之后的读取'''

	pageSource_soup=BeautifulSoup(pageSource,'lxml')
	Target=pageSource.find_all('ul')
