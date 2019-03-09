#coding=utf-8
#python趣味百题5 孪生素数
#若两个素数之差为2，则这两个素数就是孪生素数
#找出1-100之间的孪生素数
'''
设i为要找的数，
'''
def fun():
	l = []
	if True:
        	for i in range(2,100):
                	for j in range(2,i):
                        	if i % j == 0:
                                	break
                        	else:
                                	continue
                	else:
                        	l.append(i)
	print(l)
	for i in range(1,len(l)):
		if l[i] - l[i-1] == 2:
			print("%d,%d是孪生素数"%(l[i],l[i+1]))			
fun()


 
