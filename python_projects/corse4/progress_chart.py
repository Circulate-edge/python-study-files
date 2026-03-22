progress = float(input("输入进度:"))
num_star = int(progress * 60)
for i in range(20):#输出下载提示
    print("=" , end = "")
if progress < 1:
    print("开始下载", end = "")
elif progress == 1:
    print("下载完成", end="")
for i in range(20):
    print("=" , end = "")
print("\n{:.2%}".format(progress) , end= "[")#用format语句输出进度
for i in range(num_star):#用遍历循环控制输出星号个数
    print("*" , end = "")
for i in range(60 - num_star):
    print("." , end = "")
print("]" , end = "\n")#换行
for i in range(46):
    print("=" , end="")