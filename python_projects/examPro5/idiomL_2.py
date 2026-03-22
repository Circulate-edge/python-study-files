idioms = ["万事如意", "发愤图强", "笑容满面", "意气风发", "强颜欢笑", "大动干戈", "波涛汹涌", "面露喜色"]
idm_used = []  # 创建空列表存放接龙的词
idm_used.append(idioms.pop(0))  # 将第一个词从idioms[]存入idm_used[]
while True:
    count = 0  # 计数
    last_char = idm_used[-1][-1]  # 查找最后一个字符串最后一个字符
    for i in idioms:
        first_char = i[0]  # i字符串第一个字符
        if last_char == first_char:  # 匹配
            idioms.remove(i)  # 移除i串
            idm_used.append(i)  # 将i加入接龙
            count = 0
            break
        else:
            count += 1
    if count == len(idioms):  # 不匹配成语数量等于剩余词库长度时结束
        break
print(idm_used)
print(f"剩余的词:{idioms}")