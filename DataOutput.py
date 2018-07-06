import xlsxwriter
import os
import re

moduleAddress=os.path.abspath(__file__)
rawFileAddress=moduleAddress[:moduleAddress.find(r'\DataOutput.py')]+'\\'+'rawFile'
fileNumber=0
row=0  # 列
col=0  # 行
startRow=0
rowIndent=0


def dataOutput(workbook_name):
	global worksheet,row,rowIndent,startRow,fileNumber
	workbook=xlsxwriter.Workbook(workbook_name+'.xlsx')
	for rawDataFolder in os.listdir(rawFileAddress):
		print(rawDataFolder)
		for fn in os.listdir(rawFileAddress+'\\'+rawDataFolder):  # fn 表示的是文件名
			fileNumber+=1
		print('文件数量=',fileNumber)
		worksheet=workbook.add_worksheet(rawDataFolder)
		for rawDataFile in os.listdir(rawFileAddress+'\\'+rawDataFolder):
			print(rawDataFile)
			rawData=open(rawFileAddress+'\\'+rawDataFolder+'\\'+rawDataFile,mode='r',encoding='utf-8')
			rawData=rawData.read()
			character=rawData.split('~')
			rowIndentStr=re.sub("\D","",character[1])  # 获得一版邮票有几张的信息
			for partialIndent in rowIndentStr:
				rowIndent+=int(partialIndent)
			if rowIndentStr[0:1]!=rowIndent:
				print('共{}枚/张'.format(rowIndent))
			# print(rowIndent)
			# rowIndent=filter(str.isdigit,character[1])
			startRow=mergeANDwrite(worksheet,character,rawDataFile)
			rowIndent=0
		startRow=0
		rowIndent=0
		fileNumber=0
	workbook.close()


def mergeANDwrite(worksheet,character,rawDataFile):
	#  merge_range(first_row, first_col, last_row, last_col, data[, cell_format])
	#  row:一列中x位； col:一行中x位

	# @全套枚数~4枚~全套面值~4.80元~小型张规格~ 
	# ~发行日期~2012年11月30日~防伪方式~防伪纸张 防伪油墨 异形齿孔 荧光喷码~小全张规格~ 
	# ~印 刷 厂~北京邮票厂~设 计 者~汪涛~小本票编号~ 
	# ~印刷版别~影写~责任编辑~陈宜思~小本票规格~ 
	# ~摄 影 者~ ~整版枚数~16枚（4枚连印，4套）~原画作者~ 
	# ~资料提供~上海博物馆、四川博物院、浙江省博物馆、国家图书馆、审计博物馆~整张规格~190×180毫米~雕 刻 者~ 
	# ~单枚信息~(此为第37个信息,[36])


	global row,col,currentRowCount
	for currentRow in range(startRow,startRow+11+rowIndent):
		if currentRow-startRow==0:
			worksheet.merge_range(currentRow,0,currentRow,8,rawDataFile[:rawDataFile.find('.txt')])
		if currentRow-startRow==1:
			worksheet.write(currentRow,0,'总编号')
			worksheet.write(currentRow,4,'志号')
			worksheet.write(currentRow,7,'邮票名称')
			worksheet.write(currentRow,8,rawDataFile[8:rawDataFile.find('.txt')])
			worksheet.merge_range(currentRow,1,currentRow,3,'')
			worksheet.merge_range(currentRow,5,currentRow,6,rawDataFile[:8])
		if currentRow-startRow>=2 and currentRow-startRow<=7:
			worksheet.write(currentRow,0,character[(currentRow-startRow-2)*6])
			worksheet.write(currentRow,4,character[(currentRow-startRow-2)*6+2])
			worksheet.write(currentRow,7,character[(currentRow-startRow-2)*6+4])
			worksheet.write(currentRow,8,character[(currentRow-startRow-2)*6+5])
			worksheet.merge_range(currentRow,1,currentRow,3,character[(currentRow-startRow-2)*6+1])
			worksheet.merge_range(currentRow,5,currentRow,6,character[(currentRow-startRow-2)*6+3])

		# (后为第39个信息,[38])~图序~邮票名称~面值(元)~发行量~邮票规格~齿 孔 度~备注
		# ~（4-1）T~审计萌芽~1.20~
		# 1080.00万枚~40×30毫米~13×13~ 
		# ~（4-2）T~古代审计~1.20~
		# 1080.00万枚~40×30毫米~13×13~ 
		# ~（4-3）T~红色审计~1.20~
		# 1080.00万枚~
		# 40×30毫米~13×13~ 
		# ~（4-4）T~当代审计~1.20~
		# 1080.00万枚~40×30毫米~13×13~ ~
		if currentRow-startRow>=8 and currentRow-startRow<=(8+rowIndent):
			if currentRow-startRow==8:
				worksheet.merge_range(currentRow,1,currentRow,2,character[38])
				worksheet.write(currentRow,3,character[39])
				worksheet.write(currentRow,4,character[40])
				worksheet.write(currentRow,5,character[41])
				worksheet.write(currentRow,6,character[42])
				worksheet.write(currentRow,7,character[43])
				worksheet.write(currentRow,8,character[44])
			elif currentRow-startRow>8:
				worksheet.merge_range(currentRow,1,currentRow,2,character[(currentRow-startRow-9)*7+45])
				worksheet.write(currentRow,3,character[(currentRow-startRow-9)*7+45+1])
				worksheet.write(currentRow,4,character[(currentRow-startRow-9)*7+45+2])
				worksheet.write(currentRow,5,character[(currentRow-startRow-9)*7+45+3])
				worksheet.write(currentRow,6,character[(currentRow-startRow-9)*7+45+4])
				worksheet.write(currentRow,7,character[(currentRow-startRow-9)*7+45+5])
				worksheet.write(currentRow,8,character[(currentRow-startRow-9)*7+45+6])
		worksheet.merge_range(8+startRow,0,startRow+8+rowIndent,0,character[36])
		if currentRow-startRow==9+rowIndent:
			worksheet.write(currentRow,0,'样图')
			worksheet.merge_range(currentRow,1,currentRow,8,'')
		col=0
	return startRow+10+rowIndent


#  dataOutput('邮票整理结果')
#  print("get pathname:",os.path.dirname(r"C:\Users\user\Desktop\FTC\2018个人项目\数据爬虫\360doc-spider\urlList"))
