def prime(n):
    """
    判断n是素数吗
    :param n: 传入一个大于等于2的整数
    :return: boolean
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

#  主程序，哥德巴赫猜想
if __name__ == '__main__':
    n = int(input())
    #  对于大于2的偶数，判断是否满足哥德巴赫猜想，即可写为两素数之和，并输出所有可能的解
    if n > 2 and (n & 1) == 0:
        for i in range(2,n//2+1):
            if prime(i) and prime(n-i):
               print(f"{i}+{n-i}={n}")
    #  对输入错误提示
    else:
        print("ERROR")