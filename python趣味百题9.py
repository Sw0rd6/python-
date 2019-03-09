#coding=utf-8
#python趣味百题9 回文数 一个数正读和倒读都一样
#判断一个数是不是回文数
'''
思路：
98789 -> 98789
def fun(n):	
'''
def fun(n):
	ls = []
	while n > 0:
		m = n % 10
		n //= 10
		ls.append(m)
	#print(ls)
	for i in range(len(ls) // 2):
		#print(ls[i])
		#print(ls[(-i - 1)])
		if ls[i] == ls[(-i - 1)]:
			continue
		else:
			return False
	return True		 
a = fun(7675)
print(a)
	 
