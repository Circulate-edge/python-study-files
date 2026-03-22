"""
要求根据输入的夫妻 / 伴侣关系和派对宾客列表，找出派对中落单的客人（即伴侣未一同参加派对的宾客）。
"""
#  已知伴侣对数
n = int(input())
couple_dict = dict()
for i in range(n):
    a, b = input().split()
    couple_dict[a] = b
    couple_dict[b] = a
#  m位客人id
m = int(input())
guest_set = set(input().split())
single = list()
#  遍历宾客列表
for i in guest_set:
    #  i没有伴侣或伴侣不在列表中时，加入单身列表
    if i not in couple_dict or couple_dict[i] not in guest_set:
        single.append(i)
#  按id排序
single.sort()
print(len(single))
for i in range(len(single)):
    if i < len(single) - 1:
        print(single[i], end=' ')
    else:
        print(single[i])