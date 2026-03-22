order = list()
while True:
    name = input('请输入商品名称（0键退出）：')
    try:
        if name != '0':
            amount = int(input('请输入商品数量：'))
            assert amount > 0
            order.append({f'{name}': f'{amount}'})
        else:
            break
    except ValueError as error:
        print('商品数量必须为数字！', error)
    except AssertionError:
        print('商品数量至少为1！')
        order.append({f'{name}': 1})
print(order)
