#!/usr/bin/Python
# -*- coding:utf-8 -*-


import urllib
import urllib2
def main():
	url='http://www.runoob.com/python/python-socket.html'

	req=urllib2.Request(url)
	print(req)
main();