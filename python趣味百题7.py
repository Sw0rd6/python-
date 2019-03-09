#coding=utf-8
#python趣味百题7 等差素数数列
#类似 7 37 67 97 或者107 137 167 197这样由素数组成的数列叫做等差素数数列
#首先是求出指定范围以内所有的素数
#然后再去取a0，a1，这个是任意的，所以要在素数列表里面找
#下题求的是200以内的所有等差素数数列

def fun():
	l = []
	if True:
        	for i in range(2,200):
                	for j in range(2,i):
                        	if i % j == 0:
                                	break
                        	else:
                                	continue
                	else:
                        	l.append(i)
	print(l)
	le = []
	for k in range(1,len(l)):
		for p in range(k,len(l)):
			m = l[p] - l[k-1]
			temp = l[p] + m
			if temp in l:
				le = [l[k-1],l[p],temp]
				while temp + m in l:
					le.append(temp + m)
					temp += m
				print(le)
				del le
				
				
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]	
fun()

