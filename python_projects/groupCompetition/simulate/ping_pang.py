"""
洛谷NOIP2003 乒乓球
"""
import sys

# 读取信息
sco = []
for line in sys.stdin:
    line = line.strip()
    if 'E' not in line:
        sco.append(line)
    else:
        ind = line.index('E')
        sco.append(line[:ind])
        break

sco = "".join(sco)
# 打印比分
def prt_sco(system):
    p1 = 0
    p2 = 0
    for i in range(len(sco)):
        if sco[i] == 'W':
            p1 += 1
        elif sco[i] == 'L':
            p2 += 1
        if (p1 >= system or p2 >= system) and abs(p1 - p2) >= 2:
            print(f"{p1}:{p2}")
            p1 = 0
            p2 = 0
    if p1 > 0 or p2 > 0:
        print(f"{p1}:{p2}")

if sco:
    prt_sco(11)
    print()
    prt_sco(21)
else:
    print("0:0")
    print()
    print("0:0")