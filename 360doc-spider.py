import os
import DataObtain
import DataOutput
import DataPorcess
import ListObtain

mainModuleAddress=os.path.abspath(__file__)
rawAdress=mainModuleAddress[:mainModuleAddress.find(r'\360doc-spider.py')]
#  访问网址表单的确定
#  每一盒邮票有一个网页，首先以年为单位确定所有邮票的网址



#  正式访问
print(DataObtain.dataObtain(2016))