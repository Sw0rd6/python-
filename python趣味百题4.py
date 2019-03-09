#coding=utf-8
#python趣味百题4 自守数
#求10000以内的自守数？
#例子:5×5=25,6×6=36,76×76=5776等等
#思路：
'''
设自守数为i,计算i的位数l，i**2=n,n的后l位数等于i,即为所求。
'''
for i in range(1,10000):
	l,j = 1,i
	while j / 10 != 0:
		l += 1
		j /= 10
	n = i ** 2
	if n % (10 ** l) == i:
		print(i)
#多用新算法，见下，多次看到列表解析了，好用。		
#用列表解析法一行搞定
print([n for n in range(1,10000) if n * n % (10 ** len(str(n))) == n])





