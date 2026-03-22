#  定义全局变量money
from unittest import case

money = 1000
name = input("请输入姓名：")
# 定义查询函数
def query(show_header ):
    """
    查询余额
    :param show_header: 若该值为False,不打印“查询余额”提示页眉
    :return: None
    """
    if show_header:
        print(f"------------查询余额------------\n{name},您好,",end="")
    print(f"您的余额剩余: {money}元")

# 定义存款函数
def saving(save_money):
    """
    存款并调用查询,判断存入金额是否大于0,若是则存入成功，否则失败
    :param save_money: 本次存款金额
    :return: None
    """
    if save_money > 0: # 判断存款金额是否大于0，否则失败
        global money # money 在函数内部定义为全局变量
        money += save_money
        print(f"------------存款------------\n{name},您好,", end="")
        print(f"您存款{save_money}元成功" )
        query(False)
    else:
        print("存入金额必须大于0元")

# 定义取款函数
def withdraw(withdraw_money):
    """
    取款并调用查询,判断取款金额大于0成功后，判断余额是否足够
    :param withdraw_money: 本次取款金额
    :return: None
    """
    global money # money 在函数内部定义为全局变量
    if withdraw_money <= 0: # 判断取款金额是否大于0，否则失败
        print("取款金额必须大于0元")
    elif withdraw_money <= money: # 判断余额是否足够，否则失败
        money -= withdraw_money
        print(f"------------取款------------\n{name},您好,", end="")
        print(f"您取款{withdraw_money}元成功")
        query(False)
    else:
        print(f"{name},您好，您余额不足，取款{withdraw_money}元失败")
        query(False)

# 定义主菜单函数
def main():
    print(f"------------主菜单------------\n{name},您好,欢迎来到和平银行")
    print("查询余额\t请按1\n存款\t请按2\n取款\t请按3\n退出请按其他任意键")
    return int(input())

# set an unlimited cycle
while True:
    keybourd_input = main()
    match keybourd_input:
        case 1: query(True)
        case 2:
            s_money = int(input("存入(元):"))
            saving(s_money)
        case 3:
            w_money = int(input("取出(元):"))
            withdraw(w_money)
        case _: break