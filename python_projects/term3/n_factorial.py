n = int(input("输入整数："))
outcome = 1
for i in range(n, 0, -1):
    outcome *= i
print(f"{n}的阶乘是{outcome}")