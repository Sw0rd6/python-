#coding-utf-8
#python趣味百题6 可逆素数
#找出1-1000内的所有可逆素数
#可逆素数是指一个素数的各位数值顺序颠倒后得到的数仍为素数，如113和311
#思路：
'''
应该先判断位数吧，设此数为n，
if n / 10 != 0:
	l += 1
	n /= 10
print(l) #求几位数

s = n / 10
m = n % 10 #取个位数
nn = m * (10 ** l) + s
if 



'''

def fun():
	l = []
	if True:
                for i in range(10,1000):
                        for j in range(2,i):
                                if i % j == 0:
                                        break
                                else:
                                        continue
                        else:
                                l.append(i)
	print(l)
	for n in l:
		le = 0
		temp = n
		while temp // 10 > 0:
        		le += 1
        		temp //= 10
		#print(le) #求几位数
		if le >= 2:
			r = n // 100
			s = n // 10 % 10
		else:
	
			s = n // 10 #取十位数
		m = n % 10 #取个位数
		if le >= 2:
			nn = m * (10 ** le) + s * (10 ** (le-1)) + r
		else:
			nn = m * (10 ** le) + s
		if nn in l and nn != n:
			print("%d和%d为可逆素数"%(n,nn))
			l.remove(nn)
fun()

#视频介绍的算法不算好，总体算法还是用以上的，不过学到了一个细节：
'''
比如有一个数n=123
要变成321，可以简单地用索引操作和int、str的函数来操作：

n = 123
print(int(str(n)[::-1]))
就得到321了
'''
n = 123
print(int(str(n)[::-1]))






