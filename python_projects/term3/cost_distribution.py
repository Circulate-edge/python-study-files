order = input("请输入地区编号 华东地区(01) 华南地区(02) 华北地区(03)：")
weight = float(input("寄件质量(kg)"))
if order == "01":
    first_price = 13
    left = 3
elif order == "02":
    first_price = 12
    left = 2
elif order == "03":
    first_price = 14
    left = 4
else:
    print("请输入正确格式！")
if 0 < weight <= 1:
    cost = first_price
elif weight > 1:
    cost = first_price + left * (weight - 1)
else:
    print("重量必须大于0！")
print("物流费用：",round(cost,2))