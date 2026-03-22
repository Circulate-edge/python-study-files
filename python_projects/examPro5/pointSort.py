"""
5.如今两年偶像选秀节目风头正盛，吸引了许多喜欢唱跳、有一颗明星梦想的少年少女参加，青春有你正是节目之一。
青春有你采用计票机制，选手获得的票数越多，排名就越靠前。
本实例要求编写程序，接收选手的姓名和票数，输出排序后的成绩。
"""
participants = [] # 记录选手姓名及成绩
while True: # 控制输入选手数量
    ctr = input("加入成绩输入1，退出输入其他：")
    if ctr == "1":
        name, score = input("输入选手姓名 票数(用空格隔开)").split()
        participants.append({"姓名": name, "票数": int(score)}) # 列表嵌套字典存储选手票数
    else:
        break
# 定义函数
def score_get(dict):
    """
    获取字典中选手得票
    :param dict: 记录选手姓名票数的字典
    :return:
    """
    return dict["票数"]
participants.sort(key=lambda p:p["票数"], reverse=True)
for p in participants:
    print(f"{p['姓名']}:\t{p['票数']}")
"""
sort_ptc = [participants[0]] # 创建列表存储排序后成绩
for j in range(0, len(participants)):
    sort_score = 0 # 定义变量记录最高票数
    find = False
    for p in participants: # 设置循环
        if p["票数"] > sort_score and p not in sort_ptc:
            sort_score = p["票数"]
            find = True
    if find:
        sort_ptc.append(p) # 将最高票数添加入排序后成绩列表
        participants.remove(p)
"""

