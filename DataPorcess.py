from bs4 import BeautifulSoup


def dataProcess(pageSource,fileAddress):
	pageSource_soup=BeautifulSoup(pageSource,'lxml')  # 将获取的网页信息保存成BeautifulSoup对象
	contentString='@'  # 特殊标识文件以@形式开启
	table=pageSource_soup.find_all('table')[1]  # 由于需求信息存在于网页的ta_name为table的内容下，专门搜索本内容
	#  print(table)
	if table.attrs['id']=='table7961':
		for line in table.find_all('td'):
			contentString+=line.get_text()+'~'
		print('target content in string')
	else:
		print('unable to find target content')
	fileName=pageSource_soup.find('h2').string
	file=open(fileAddress+"\\"+fileName+'.txt',mode='w',encoding='utf-8')
	file.write(contentString)
	file.close()
	return contentString


#  print(dataProcess(html_doc))
