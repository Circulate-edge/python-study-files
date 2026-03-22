drink_menu = {'cococola':2.5,
              'pessiecola':2.5,
              '冰红茶':3.0,
              '脉动':3.5,
              '果缤纷':3.0,
              '绿茶':3.0,
              '茉莉花茶':3.0,
              '尖叫':2.5}
def preview():
    """
    查看饮品菜单
    :return:
    """
    print("---------------------")
    for i in drink_menu.items():
        print(f"{i[0]}:{i[1]}")
    print("---------------------")

def order(menu):
    """
    点单
    :return:
    """
    #  订单,内用元组存储饮品名和数量
    ords = []
    while True:
        drink = input("输入饮品名称(q建退出):\n")
        if drink == "q":
            break
        elif drink not in menu:
            print("饮品名称不正确")
            continue
        else:
            while True:
                amount = input("请输入数量：")
                if not amount.isdigit():
                    print("饮品数量不合法")
                    continue
                else:
                    amount = int(amount)
                if int(amount) <= 0 or amount % 1 != 0:
                    print("饮品数量不合法")
                    continue
                else:
                    ords.append((drink,amount))
                    break
    return ords

def pay(ords):
    print("名称".center(12),"价格".center(12),"数量".center(12))
    cost = 0
    for i in ords:
        print(i[0].center(12),str(drink_menu[i[0]]).center(12),str(i[1]).center(12),sep='')
        cost += drink_menu[i[0]] * i[1]
    print("总价{:.2f}元".format(cost))

preview()
ords = order(drink_menu)
pay(ords)