year = int(input("输入年份: "))
month = int(input("输入月份: "))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("%d月有31天" % month)
elif month in [4, 6, 9, 11]:
    print("%d月有30天" % month)
elif month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("%d月有29天" % month)
    else:
        print("%d月有38天" % month)