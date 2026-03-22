count = 0
def hanota(n: int, start ,mid, end):
    global count
    if n < 1:
        print("无圆盘可移动")
    elif n == 1:
        count += 1
        print(f"第{n}个圆盘从{start}柱移动到{end}柱")
    elif n == 2:
        count += 1
        print(f"第{n - 1}个圆盘从{start}柱移动到{mid}柱")
        count += 1
        print(f"第{n}个圆盘从{start}柱移动到{end}柱")
        count += 1
        print(f"第{n - 1}个圆盘从{mid}柱移动到{end}柱")
    else:
        hanota(n - 1, start, end, mid)
        count += 1
        print(f"第{n}个圆盘从{start}柱移动到{end}柱")
        hanota(n - 1, mid, start, end)

num = int(input("输入圆盘数"))
hanota(num, 'A', 'B', 'C')
print(f"共{count}步")