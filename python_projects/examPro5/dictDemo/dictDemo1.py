"""
统计字符串中单个字符出现频率
"""
string = input()
char = dict()
for i in string:
    if i not in char:
        char[i] = 1
    else:
        char[i] += 1
for key in char:
    print(f"{key}:{char[key]}")