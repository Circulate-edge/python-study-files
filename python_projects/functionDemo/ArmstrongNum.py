def armstrong(n):
    for i in range(10**(n-1),10**n):
        sum = 0
        temp = i
        """        
        for _ in range(n):
            sum += (i % 10)**n
            i = i // 10
        """
        for j in str(i):
            sum += int(j)**n
        if sum == temp:
            print(f"{temp}是Armstrong数")
n = int(input("输入位数:"))
armstrong(n)