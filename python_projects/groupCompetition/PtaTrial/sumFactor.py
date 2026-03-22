# 输入一个正整数，求它的约数个数和约数和
n = int(input("输入正整数:"))
factor_num = 0
factor_sum = 0
# 一个数 n 的因数具有成对出现的特性：
# 若 i 是 n 的因数，则 n/i 必然也是 n 的因数（例如 6 的因数对：(1,6)、(2,3)）。
# 基于此特性，遍历范围无需到 n，只需到 √n（根号 n）即可 —— 因为超过 √n 的因数，必然是前面已找到因数的 “配对因数”，无需重复判断。
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        factor_num += 1
        factor_sum += i
        # 配对因数
        pair_fact = n / i
        if pair_fact != i:
            factor_num += 1
            factor_sum += pair_fact
print("约数个数：{}，约数和：{}".format(factor_num, int(factor_sum)))
