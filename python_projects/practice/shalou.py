"""n = int(input("输入方阵阶数:")) # 设置行数n
for i in range(1,n+1): # 行标为i,i=1,2...n
    for j in range(1,n+1): # 列标为j,j=1,2...n
# 输出n*n的矩阵
        if j < n: # 列指标小于n时,输出*,不换行
            print("*",end="")
        elif j == n: # 列指标为n时,输出*,且换行
            print("*",end="\n")"""
n = int(input("输入方阵阶数:")) # 设置行数n
k = n  # 第一行输出n个*
space = 0  # 第一行两边" "数量为0
for i in range(1,n+1):  #行标为i,i=1,2...n
    # 第一行输出n个*,后一行输出n-2个*,依次递减,至第i行输出k个*号(i <= n // 2 and (k - 2) >= 1)
    if i <= n // 2 and (k - 2) >= 1:
        for space_l in range(space):
            print(" ", end="")
        for star in range(k):
            print("*",end="")
        for space_r in range(space):
            print(" ", end="")
        k -= 2
        space += 1
    elif i > n // 2 and (k + 2) <= n:
        for space_l in range(space):
            print(" ", end="")
        for star in range(k):
            print("*",end="")
        for space_r in range(space):
            print(" ", end="")
        k += 2
        space -= 1
    else:
        for space_l in range(space):
            print(" ", end="")
        for star in range(k):
            print("*",end="")
        for space_r in range(space):
            print(" ", end="")
    # 最后一列换行
    print("",end="\n")