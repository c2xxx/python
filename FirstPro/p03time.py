#!/usr/bin/python
#-*- coding:UTF-8 -*-

import datetime as cc
import datetime  
import time  
print('中文')

if __name__ =='__main__':
	#输入今天日期，格式dd/mm/yyyy
	print('今天日期：')
	print(datetime.date.today().strftime('%d/%m/%y'))

	#创建日期对象
	miyazakiBirthDate= datetime.datetime(1991,11,1,2,3,4)

	print('生日：')
	print(miyazakiBirthDate.strftime('%Y-%m-%d %H:%M:%S')) 
	#日期计算
	miyazakiBirthDate=miyazakiBirthDate+datetime.timedelta(days=100)
	print('百天：')
	print(miyazakiBirthDate.strftime('%Y-%m-%d %H:%M:%S')) 

	print('当前时间：')
	print(cc.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) 
	print('原始时间戳：')
	print(time.time()) 
	print('秒级时间戳：')
	print(int(time.time()))  