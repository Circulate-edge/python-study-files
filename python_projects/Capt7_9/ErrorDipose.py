while True:
    divised = input("输入被除数：")
    divise = input("输入除数：")
    try:
        divised = int(divised)
        divise = int(divise)
        break
    except ValueError as error:
        print(f"出错：{error}\n请重新输入")

try:
    assert divise != 0, "除数不为0"
    res = divised / divise
except AssertionError as error:
    print(f"程序出错，错误信息：{error}")
else:
    print(res)