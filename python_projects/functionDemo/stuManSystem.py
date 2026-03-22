"""
学生管理系统
"""
students = {}
#   添加信息
def add_info():
    name = input("请输入学生姓名：")
    gender = input("请输入学生性别：")
    phone = input("请输入学生手机号：")
    if name == "" or gender == "" or phone == "":
        print("输入不能为空")
    else:
        students[order] = [name, gender, phone]
        print("保存成功")
# 主程序循环
while True:
    # 显示菜单选项
    print("-------学生管理系统--------")
    choice = int(input("1.添加学生信息\n"
              "2.删除学生信息\n"
              "3.修改学生信息\n"
              "4.查询学生信息\n"
              "5.查看所有学生信息\n"
              "0.退出系统\n"))
    match choice:
        case 1: # 添加学生信息
            order = input("请输入学号：")
            if order in students:
                print("学号已存在")
            else:
                add_info()
        case 2: # 删除学生信息
            order = input("请输入学号：")
            if order not in students:
                print("学号不存在")
            else:
                del students[order]
        case 3: # 修改学生信息
            order = input("请输入学号：")
            if order not in students:
                print("学号不存在")
                continue
            add_info()
        case 4: # 查询学生信息
            order = input("请输入学号：")
            if order not in students:
                print("学号不存在")
            else:
                print(f"{order}: {students[order]}")
        case 5: # 查看所有学生信息
            students = dict(sorted(students.items()))
            for order in students:
                print(f"{order}\t"
                      f"{students[order][0]}\t{students[order][1]}\t{students[order][2]}\t")
        case _: # 退出系统
            print("退出系统")
            break