print("===== 成绩评定系统 =====")
print("输入分数（0-100）查看等级，输入 'q' 退出程序\n")

# while循环实现持续输入，直到输入q退出
while True:
    #  获取用户输入
    score_input = input("请输入成绩（或输入q退出）：").strip()

    #  退出条件判断：输入q则终止循环
    if score_input.lower() == 'q':
        print("程序已退出，感谢使用！")
        break

    try:
        score = float(score_input)
    except ValueError:
        print("输入错误！请输入数字。")
        continue

    #  分数范围校验
    if score < 0 or score > 100:
        print("分数超出范围！请输入0-100之间的数字。")
        continue

    #  判断等级
    if score >= 90:
        level = "优秀"
    elif score >= 80:
        level = "良好"
    elif score >= 60:
        level = "及格"
    else:
        level = "不及格"

    #  输出评定结果
    print(f"成绩：{score} → 等级：{level}\n")