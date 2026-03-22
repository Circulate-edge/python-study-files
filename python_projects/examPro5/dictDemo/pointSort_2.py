#  输入选手
n = int(input("输入选手人数："))
pla_poi = dict()
for i in range(n):
    name,points = input("输入选手姓名，票数(用空格隔开)").split()
    pla_poi[name] = points
#  排序
pla_poi = dict(sorted(pla_poi.items(), key=lambda x: x[1]))
for i in pla_poi.items():
    print(f"{i[0]}:\t{i[1]}")