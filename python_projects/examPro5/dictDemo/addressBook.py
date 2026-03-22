"""
通讯录是记录了联系人姓名和联系方式的名录，手机通讯录是最常见的通讯录之一，人们可以在通讯录中通过姓名查看相关联系人的联系方式等信息，也可以在其中新增联系人，或修改、删除联系人信息。
可以通过姓名查看联系人手机号、电子邮箱、联系地址，也可新增、修改、删除联系人等。
"""
address_book = dict()  # 通讯录
#  定义查看通讯录的函数
def content_access():
    """
    读取通讯录
    :return: None
    """
    if len(address_book) == 0:
        print("通讯录无信息")
    else:
        print("-----通讯录------")
        for x,y in address_book.items():
            print(f"{x}: {y}")

#   定义删除联系人的函数
def content_delete(pr_del):
    """
    删除联系人
    :param pr_del: 是否打印删除成功提示
    """
    if len(address_book) == 0:
        print("通讯录无信息")
    else:
        name = input("联系人姓名：")
        if name in address_book:
            del address_book[name]
            if pr_del:
                print("-----删除成功-----")
        else:
            print("联系人不在通讯录中")

#  添加、修改联系人
def content_add():
    """
    按照提示添加或修改联系人信息
    :return:
    """
    name = input("新联系人姓名：");
    phone = input("新联系人手机号：")
    ema = input("新联系人电子邮箱：");
    address = input("新联系人地址：")
    if name == "" or phone == "" or ema == "" or address == "":
        print("用户信息不能为空！")
    else:
        address_book[name] = {"电话": phone, "邮箱": ema, "联系地址": address}
        print("保存成功")
#  程序主入口
while True:
    cho = input("添加联系人(输入1)\t查看通讯录(输入2)\n"
                "删除联系人(输入3)\t修改联系人(输入4)\n"
                "查找联系人(输入5)\t退出(输入其他)\n")
    if cho == "1":  # 添加联系人(输入1)
        content_add()
    elif cho == "2":  # 查看通讯录(输入2)
        content_access()
    elif cho == "3":  # 删除联系人(输入3)
        content_delete(True)
    elif cho == "4":  # 修改联系人(输入4)
        content_delete(False)
        content_add()
    elif cho == "5":  # 查找联系人(输入5)
        if len(address_book) == 0:
            print("通讯录无信息")
        else:
            name = input("联系人姓名：")
            if name in address_book:
                print(f"{name}: {address_book[name]}")
            else:
                print("联系人不在通讯录中")
    else:
        break