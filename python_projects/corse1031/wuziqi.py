#i为行数
#j为列数
n = int(input("请输入棋盘大小："))
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            print('┌',end='')
