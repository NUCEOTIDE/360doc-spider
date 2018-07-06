from bs4 import BeautifulSoup


isObtained=False


def dataProcess(pageSource,fileAddress):
	'''处理保存在字符串中的原始数据，输出数据保存在txt格式文件中'''

	global isObtained
	pageSource_soup=BeautifulSoup(pageSource,'lxml')  # 将获取的网页信息保存成BeautifulSoup对象
	contentString='@'  # 特殊标识文件以@形式开启
	table=pageSource_soup.find_all('table')[1]  # 由于需求信息存在于网页的ta_name为table的内容下，专门搜索本内容
	try:
		for line in table.find_all('td'):
			isObtained=True
			if line.get_text()=='同时发行':
				break
			else:
				contentString+=line.get_text()+'~'
		if isObtained:
			print('目标内容已转移自字符串中')
		else:
			print('无法找到目标内容')
	except FileNotFoundError:
		print('无法找到文件')
		return

	fileName=pageSource_soup.find('h2').string  # 创建新文件
	file=open(fileAddress+"\\"+fileName+'.txt',mode='w',encoding='utf-8')
	file.write(contentString)  # 将结果写入文件
	file.close()  # 关闭文件
	print('{}\n 文件创建并写入成功'.format(fileName))
	return

