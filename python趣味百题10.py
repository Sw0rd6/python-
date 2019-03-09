#coding=utf-8
#python趣味百题10 埃及分数式
#埃及分数式：只使用分子是1的分数，因此这种分数也叫作埃及分数式
#举个栗子：3/7 = 1/3 + 1/11 + 1/231
#要求输入一个真分数，将该分数分解为埃及分数式
def fun(a,b):
	ls = []
	k = int(b / a)
	if b % a == 0:
		res = '1 / %s' % k
	else:
		k += 1
		res = '1 / %s + %s' % (k, fun(a * k -b, b * k))
	return res
a,b = eval(input()),eval(input())
print("%d / %d = "%(a,b) + fun(a,b))
#以上可以自定义输入，还能看到输入的结果，加个eval(input())即可
