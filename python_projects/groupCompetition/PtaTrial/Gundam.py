"""
计算 T 秒后钢达姆的坐标
分析命令串的循环规律：
设命令串长度为L，先计算完整循环次数：cycle = T // L
计算剩余执行次数：left = T % L
"""
#  输入命令字符串S,时间T
S = input().strip()
T = int(input())
L = len(S)

# 统计单次命令串后坐标变化
x_cycle = 0
y_cycle = 0
for c in S:
    if c == 'E':
        x_cycle += 1    #  向东
    elif c == 'W':
        x_cycle -= 1    #  向西
    elif c == 'N':
        y_cycle += 1    #  向北
    elif c == 'S':
        y_cycle -= 1    #  向南

# 完整循环的坐标变换
cycle = T // L
x = cycle * x_cycle
y = cycle * y_cycle

# 剩余命令的坐标变换
left = T % L
for i in range(left):
    c = S[i]
    if c == 'E':
        x += 1
    elif c == 'W':
        x -= 1
    elif c == 'N':
        y += 1
    elif c == 'S':
        y -= 1

print(x, y)