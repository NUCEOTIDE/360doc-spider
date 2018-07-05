from bs4 import BeautifulSoup
import os


def dataProcess(pageSource,fileAddress):
	pageSource_soup=BeautifulSoup(pageSource,'lxml')
	contentString='@'
	table=pageSource_soup.find_all('table')[1]
	print(table)
	if table.attrs['id']=='table7961':
		for line in table.find_all('td'):
			contentString+=line.get_text()+'~'
	fileName=pageSource_soup.find('h2').string
	file=open(fileAddress+fileName+'.txt',mode='w',encoding='utf-8')
	file.write(contentString)
	file.close()
	return contentString


#  print(dataProcess(html_doc))
