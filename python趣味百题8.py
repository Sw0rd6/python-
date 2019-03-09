#coding=utf-8
#python趣味百题8 赛场统分
#有n个裁判计分，打出n个评分，最终要去掉一个最高分，去掉一个最低分
#剩下的n-2个求平均值即为选手的最终打分成绩
'''
思路：
'''
def fun(n):
	import random
	ls = []
	for i in range(n):
		ls.append(random.randint(1,100))
	ls.sort()
	del(ls[0])
	del(ls[n-2])
	print(sum(ls) / (n-2))
fun(100)
