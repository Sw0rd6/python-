#coding=utf-8
#python趣味百题3
#不重复的三位数
#0-9可以组成多少个不重复的3位数？
'''
3位数的个，十，百分别表示为a,b,c
a可以取1-9,不能取0
b可以取0-9
c可以0-9
算法可以为：第一种
sum = 0
for i in range(1,1000):
	a = i % 10
	b = i / 10 % 10
	c = i/ 100
	if c == 0:
		continue
	if a == b or b == c or c == a:
		continue
	else:
		print(i)
		sum += 1
	print(sum)
'''	
def NotRepeat():
	l = range(10)
	count = 0
	for a in l[1:]:
		for b in l:
			if a == b:
				continue
			for c in l:
				if c != a and c != b:
					print(a,b,c)
					count += 1
	print(count)
NotRepeat()





