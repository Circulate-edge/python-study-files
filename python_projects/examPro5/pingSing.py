num = int(input("评委人数："))
point = []
for i in range(1, num + 1):
    point_p = float(input("第%s个评委打分：" % i))
    point.append(point_p)
point.sort()
point.pop()
point.pop(0)
score = 0
for j in point:
    score += float(j)
score = score / (num-2)
print("得分：%.2f" % score)