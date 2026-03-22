"""美团满30减10
饿了么全场9折
对比用户在哪家下单划算"""
cspt = float(input("用户消费金额"))
if cspt > 0:
    eleme = cspt * 0.9
    if cspt >= 30:
        meituan = cspt - 10
    else:
        meituan = cspt
    print("在美团的消费是{:.2f}元".format(meituan), "在饿了么的消费是{:.2f}元".format(eleme))
    if meituan >= eleme:
        print("在饿了么便宜")
    else:
        print("在美团便宜")