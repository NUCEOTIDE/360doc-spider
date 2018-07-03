from bs4 import BeautifulSoup
import DataObtain


def listObtain(new_url):
	DataObtain.request_initial(new_url)
	rawData=DataObtain.requests()
	print(rawData)
	rawData_Soup = BeautifulSoup(rawData, 'lxml')  # 声明BeautifulSoup对象
	print('finished loading beautifulsoup')
	for targetTag in rawData_Soup.find_all('div',class_='listmain'):
		tempData_url=targetTag.find('a').get('href')
		print(tempData_url)




listObtain('http://www.360doc.com/userhome/27905781')
