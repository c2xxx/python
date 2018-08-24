#-*-coding:utf8-*-
import datetime;
print('写入文件内容!')


def write(file,content):
	f=open(file,'w')#不追加
	f.write(content);

write("p05.txt",'标题');



def writeAppend(file,content):
	f=open(file,'a')#追加
	f.writelines(content);

writeAppend("p05.txt",'\n追加的内容');
writeAppend("p05.txt",'\n追加的内容2');
writeAppend("p05.txt","\n当前时间："+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"));

 
def read(file):
	f=open(file)
	line=f.readline()
	while line:
		print (line)
		line=f.readline();

read("p05.txt");