import time
import turtle

def move(x=0, y=0):  # 画笔悬空移动
    turtle.penup()  # 抬起画笔
    turtle.goto(x, y)  # 画笔移动至指定位置(x, y)
    turtle.pendown()  # 放下画笔

def create():  # 初始化时钟指针
    hand = turtle.Turtle()  # 创建时钟指针
    hand.seth(90)  # 指针向上（12点方向）
    hand.pensize(2)  # 设置指针尺寸为2
    hand.hideturtle()  # 隐藏指针箭头
    return hand  # 返回指针

turtle.pensize(5)  # 设置画笔尺寸为5
turtle.speed(10)  # 设置画笔移动的速度为10
move(0, 200)
for temp in range(0, 360, 6):
    if temp % 30 == 0:  # 绘制12小时表示的竖线
        turtle.left(90)  # 画笔向左转动90度
        turtle.forward(20)  # 画笔向前移动长度20
        turtle.backward(20)  # 画笔向后移动回到刚才位置
        turtle.penup()  # 抬起画笔
        turtle.right(90)  # 画笔向右转动90度
        turtle.circle(-200, 6)  # 画笔向下向右绘制半径为200、角度为6度的圆弧
        turtle.pendown()  # 放下画笔
    else:  # 绘制60分钟表示的圆点
        turtle.dot(5)  # 画一个尺寸为5的圆点
        turtle.penup()  # 抬起画笔
        turtle.circle(-200, 6)  # 画笔向下向右绘制半径为200、角度为6度的圆弧
        turtle.pendown()  # 放下画笔
turtle.hideturtle()  # 隐藏画笔箭头
hour_hand = create()  # 创建时针
minute_hand = create()  # 创建分针
second_hand = create()  # 创建秒针

hour0, minute0, second0 = 0, 0, 0  # 设置起始时间为0点0分0秒
week = {'Mon': '星期一', 'Tue': '星期二', 'Wed': '星期三', 'Thu': '星期四', 'Fri': '星期五', 'Sat': '星期六',
        'Sun': '星期天'}
while True:
    year = time.strftime('%Y')
    month = time.strftime('%m')
    day = time.strftime('%d')
    hour = int(time.strftime('%H'))
    minute = int(time.strftime('%M'))
    second = int(time.strftime('%S'))
    weekend = time.strftime('%a')

    move(0, 100)
    turtle.write(week[weekend], align='center', font=('宋体', 20, 'normal'))
    move(0, -50)
    turtle.write(f'{year}.{month}.{day}', align='center', font=('Times New Roman', 20, 'normal'))

    temp_h = hour - hour0
    temp_m = minute - minute0
    temp_s = second - second0
    hour_hand.right((temp_h + temp_m / 60 + temp_s / 3600) % 12 * 30)  # 时针顺时针转动
    hour_hand.forward(80)
    hour_hand.backward(100)
    hour_hand.forward(20)
    minute_hand.right((temp_m + temp_s / 60) % 60 * 6)  # 分针顺时针转动
    minute_hand.forward(130)
    minute_hand.backward(150)
    minute_hand.forward(20)
    second_hand.right(temp_s % 60 * 6)  # 秒针顺时针转动
    second_hand.forward(180)
    second_hand.backward(200)
    second_hand.forward(20)
    turtle.tracer(True)  # 开启屏幕的自动刷新

    hour0, minute0, second0 = hour, minute, second  # 设置下一时刻开始时间为上一时刻结束时间
    time.sleep(1)  # 程序挂起1秒
    turtle.tracer(False)  # 关闭屏幕的自动刷新
    hour_hand.clear()
    minute_hand.clear()
    second_hand.clear()

turtle.done()  # 结束绘制
