#!/usr/bin/Python
# -*- coding:utf-8 -*-


import urllib 
def main(): 

	url='http://www.runoob.com/python/python-socket.html'

	conn = httplib.HTTPConnection("192.168.81.16")
	conn.request(method="GET",url=url) 

	response = conn.getresponse()
	res= response.read()
	print (res)
main();