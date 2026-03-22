M = int(input("消费金额："))
S = int(input("积分："))
if M >= 1000 and S >= 10000:
    print("钻石会员")
elif 500 <= M < 1000 or 5000 <= S < 10000:
    print("白金会员")
elif 200 <= M < 500 or 2000 <= S < 5000:
    print("黄金会员")
elif 100 <= M < 200 or 1000 <= S < 2000:
    print("白银会员")
elif 50 <= M < 100 or 500 <= S < 1000:
    print("青铜会员")
elif M < 50 or 0 <= S < 500:
    print("普通会员")