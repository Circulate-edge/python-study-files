import time
import turtle

# print(time.localtime()[:6])
# print(time.strftime("%y-%m-%d %H:%M:%S"))

# 创建图形窗口
turtle.setup()

def move(x=0, y=0):  # 画笔悬空移动
    turtle.penup()  # 抬起画笔
    turtle.goto(x, y)  # 画笔移动至指定位置(x, y)
    turtle.pendown()  # 放下画笔

# 设置画笔
turtle.pensize(5)
turtle.color()
turtle.speed(10)

# 绘制钟盘
move(0, 350)
turtle.fillcolor("#094E78")
turtle.begin_fill()
turtle.circle(-350)
turtle.end_fill()
move(0,300)
for temp in range(0, 60):
    if temp % 5 == 0:
        turtle.left(90)
        turtle.forward(20)
        turtle.backward(20)
        turtle.penup()
        turtle.right(90)
        turtle.circle(-300, 6)
        turtle.pendown()
    else:
        turtle.dot(5)  # 画一个尺寸为5的圆点
        turtle.penup()  # 抬起画笔
        turtle.circle(-300, 6)
        turtle.pendown()  # 放下画笔
turtle.hideturtle()

# 创建指针对象
def point():
    hand = turtle.Turtle()  # 创建指针对象
    hand.seth(90)  # 指针向上（12点方向）
    hand.speed(10)
    hand.pensize(3)  # 设置指针尺寸为2
    hand.hideturtle()  # 隐藏指针箭头
    return hand  # 返回指针

hour_point = point()
hour_point.pensize(4)
minute_point = point()
second_point = point()
second_point.pensize(2)

week = {'Mon': '星期一', 'Tue': '星期二', 'Wed': '星期三',\
        'Thu': '星期四', 'Fri': '星期五',\
        'Sat': '星期六', 'Sun': '星期天'}

hour0, minute0, second0 = 0, 0, 0  # 设置起始时间为0点0分0秒
while True:
    year = time.strftime('%Y')
    month = time.strftime('%m')
    day = time.strftime('%d')
    hour = int(time.strftime('%H'))
    minute = int(time.strftime('%M'))
    second = int(time.strftime('%S'))
    weekend = time.strftime('%a')

    # 打印日期
    move(0, 50)
    turtle.pencolor("#62BFC7")
    turtle.write(week[weekend], align='center', font=('宋体', 20, 'normal'))
    move(0, -50)
    turtle.write(f'{year}年{month}月{day}日', align='center', font=('Times New Roman', 20, 'normal'))

    temp_hour = hour - hour0
    temp_minute = minute - minute0
    temp_second = second - second0
    hour_point.right((temp_hour + temp_minute / 60 + temp_second / 3600) %12 * 30) # 将24小时转为12小时后转相应角度
    hour_point.forward(120)
    hour_point.backward(140)
    hour_point.forward(20)  # 指针归位
    minute_point.right((temp_minute + temp_second / 60) % 60 * 6)  # 将24小时转为12小时后转相应角度
    minute_point.forward(180)
    minute_point.backward(200)
    minute_point.forward(20)
    second_point.right(temp_second * 6)  # 将24小时转为12小时后转相应角度
    second_point.forward(250)
    second_point.backward(270)
    second_point.forward(20)
    turtle.tracer(True)  # 开启屏幕的自动刷新

    # 更新初始时刻
    hour0 = hour
    minute0 = minute
    second0 = second
    time.sleep(1)
    turtle.tracer(False)  # 关闭屏幕的自动刷新
    # 清理指针
    hour_point.clear()
    minute_point.clear()
    second_point.clear()

# 绘制结束
turtle.done()