def fib(n: int):
    """
    递归实现斐波那契数列
    :param n: 第n 项,即第n个月份
    :return: 兔子总对数
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("月份:"))
if n > 0:
    print(f"第{n}个月的兔子总数是{fib(n)}")
else:
    print("输入不合法")