#coding=utf-8
#python趣味百题2 水仙花数（100-999）
#这种算法可移植性太差了！可以用其他算法，直接改range（）就能获得其他需求
def fun(n):
	a = n / 100
	b = n / 10 % 10
	c = n % 10
	if a ** 3 + b ** 3 + c ** 3 == n:
		print(n)
for i in range(100,1000):
	fun(i)
e=[1,3,5,7,9]
print([x ** 3 for x in e])
print(sum([x ** 3 for x in e]))
#以上用到列表解析：
'''
a=[1,3,5,7,9]
sum([x ** 3 for x in a])	
'''

