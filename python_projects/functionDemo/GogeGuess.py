count = 0
def Gogue(n):
    global count
    if n == 1:
        print(f"结果:{n},运行次数{count}")
    elif (n & 1) == 1: # n为奇数
        count += 1
        n = n * 3 + 1
        print(f"第{count}次结果:{n}")
        return Gogue(n)
    elif (n & 1) == 0: # n为偶数
        count += 1
        n = int(n / 2)
        print(f"第{count}次结果:{n}")
        return Gogue(n)

n = int(input("输入正整数"))
if n > 0:
    Gogue(n)
else:
    print("输入不合法")