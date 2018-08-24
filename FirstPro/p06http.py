#！coding:utf8  
print("http请求")
import urllib.request

 
def saveHttpContent(file,content):
	f=open(file,'w',encoding="utf-8")#不追加
	f.writelines(content);

# response = urllib.request.urlopen(url)
# print(response.status)
# # print(response.read())
 

def doRequest(url,fileName): 
	response = urllib.request.urlopen(url)
	print("status:")
	print(response.status)
	print("getheaders:")
	print(response.getheaders())
	print("Server:")
	print(response.getheader("Server"))
	content=response.read().decode("utf-8")
	print(content)
	saveHttpContent(fileName,content)
  
 
url1='https://suggest.taobao.com/sug?code=utf-8&q=%E9%A3%9E%E6%9C%BA'
url2='https://suggest.taobao.com/sug?code=utf-8&q=iphone'
url3='https://www.baidu.com'

doRequest(url1,"p06http1.txt");
doRequest(url2,"p06http2.txt");
doRequest(url3,"p06http3.txt");
