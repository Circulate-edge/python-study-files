year = int(input("输入年份："))
month = int(input("输入月份："))
day = int(input("输入天数："))
hour = int(input("输入小时："))
minute = int(input("输入分钟："))
second = int(input("输入秒钟："))
while True:
    region = input("输入地区(中国:01/美国:02/英国:03/澳大利亚:04/法国:05/德国:06/俄罗斯:07/加拿大:08)(退出:exit):")
    if region == "01":
        print("{:04d}年{:02d}月{:02d}日  {:02d}:{:02d}:{:02d}".format(year,month,day,hour,minute,second))
    elif region == "02":
        print("{:02d}/{:02d}/{:04d}  {:02d}:{:02d}:{:02d}".format(month,day,year,hour,minute,second))
    elif region == "03" or  region == "04" or  region == "05":
        print("{:02d}/{:02d}/{:04d}  {:02d}:{:02d}:{:02d}".format(day,month,year,hour,minute,second))
    elif region == "06" or region == "07":
        print("{:02d}.{:02d}.{:04d}  {:02d}:{:02d}:{:02d}".format(day,month,year,hour,minute,second))
    elif region == "08":
        print("{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year,month,day,hour,minute,second))
    elif  region == "exit":
        break
    else:
        print ("请输入正确格式!")