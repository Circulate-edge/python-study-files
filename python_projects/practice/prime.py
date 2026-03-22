#  1到100之间所有素数

def prime(n):
    import math
    for i in range(2,n + 1):
        flag = True
        #  一个数被除至少有2个因数，找因数只用遍历到它的平方根
        for j in range(2,int(math.sqrt( i))):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(f"{i}是质数")

if __name__ == '__main__':
    n = int(input("请输入数字："))
    if n > 2:
        prime(n)
    else:
        print("请输入大于2的数字")