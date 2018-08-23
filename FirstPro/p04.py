# -*- conding utf-8 -*-

print('将一个数组逆序输出')


if __name__ =="__main__":
	a=[9,8,6,7]
	print('原始数组')
	print(a)

	N= len(a) 

	print('长度'+str(N))

	for i in range(int(len(a)/2)):
		a[i],a[N-i-1]=a[N-i-1],a[i]

	print('新的数组')
	print(a)