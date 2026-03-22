comInf = {'华为 P60': {'price':4887.00,'salVol':210},
          '华为 Mate 40E Pro': {'price':4699.00,'salVol':90},
          '华为 Nova 10 青春版': {'price':1698.00,'salVol':102},
          '华为 P50 Pro': {'price':3987.00,'salVol':88},
          '华为畅想 70': {'price':999.00,'salVol':152}}
def comInforSort(info,type):
    """
    信息排序
    :param info: 排序对象
    :param type: 排序依据（价格:1/销量:2/总价:3）
    :return: 排序后字典
    """
    for i in comInf.items():
        i[1]['amount'] = i[1]['price'] * i[1]['salVol']
    if type == '1':
        type = 'price'
    elif type == '2':
        type = 'salVol'
    elif type == '3':
        type = 'amount'
    else:
        print("输入错误")
        return
    return dict(sorted(info.items(),key=lambda x:x[1][type],reverse=True))

type = input("请选择排序依据（单价:1/销量:2/总销售额:3）:")
comInf = comInforSort(comInf,type)
print("{}\t{}\t销量\t总销售额".format("名称".center(15),"单价".center(6)))
for i in comInf.items():
    print("{}\t{}\t{}\t{}".format(i[0].center(15),str(i[1]['price']).center(6),i[1]['salVol'],i[1]['amount']))