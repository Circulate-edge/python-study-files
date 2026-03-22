while True:
    loan = input("请输入贷款类型（1）商业贷款，（2）公积金贷款，（3）组合贷款，（exit）退出")
    if loan == "exit":
        break
    money = float(input('贷款金额：'))
    year = int(input('贷款年限'))
    if loan == "1":
        if year <= 5:
            rate = 0.0475
            month = year * 12
            money_month = money * (rate / 12 * (1 + rate / 12) ** month) / ((1 + rate / 12) ** month - 1)
            money_sub = money_month * year * 12
            money_rate = money_sub - money
            print('还款总额：', round(money_sub, 2),'总利息：', round(money_rate, 2))
        else:
            rate = 0.049
            month = year * 12
            money_month = money * (rate / 12 * (1 + rate / 12) ** month) / ((1 + rate / 12) ** month - 1)
            money_sub = money_month * year * 12
            money_rate = money_sub - money
            print('还款总额：', round(money_sub, 2), '总利息：', round(money_rate, 2))
    elif loan == "2":
        if year <= 5:
            rate = 0.026
            month = year * 12
            money_month = money * (rate / 12 * (1 + rate / 12) ** month) / ((1 + rate / 12) ** month - 1)
            money_sub = money_month * year * 12
            money_rate = money_sub - money
            print('还款总额：', round(money_sub, 2), '总利息：', round(money_rate, 2))
        else:
            rate = 0.031
            month = year * 12
            money_month = money * (rate / 12 * (1 + rate / 12) ** month) / ((1 + rate / 12) ** month - 1)
            money_sub = money_month * year * 12
            money_rate = money_sub - money
            print('还款总额：', round(money_sub, 2), '总利息：', round(money_rate, 2))
    elif loan == "3":
        part = float(input('公积金贷款占比：'))
        if year <= 5:
            rate = 0.0475 * part + 0.026 * (1 - part)
            month = year * 12
            money_month = money * (rate / 12 * (1 + rate / 12) ** month) / ((1 + rate / 12) ** month - 1)
            money_sub = money_month * year * 12
            money_rate = money_sub - money
            print('还款总额：', round(money_sub, 2), '总利息：', round(money_rate, 2))
        else:
            rate = 0.049 * part + 0.031 * (1 - part)
            month = year * 12
            money_month = money * (rate / 12 * (1 + rate / 12) ** month) / ((1 + rate / 12) ** month - 1)
            money_sub = money_month * year * 12
            money_rate = money_sub - money
            print('还款总额：', round(money_sub, 2), '总利息：', round(money_rate, 2))