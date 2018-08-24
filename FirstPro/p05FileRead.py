#-*-coding:utf8-*-

print('HELLO WORLD哈哈哈!')


def read(file):
	f=open(file)
	line=f.readline()
	while line:
		print (line)
		line=f.readline();

read("p02.py");