import turtle


def move(x=0, y=0):  # 画笔悬空移动
    turtle.penup()  # 抬起画笔
    turtle.goto(x, y)  # 画笔移动至指定位置(x, y)
    turtle.pendown()  # 放下画笔


def draw(color, radius, extend, gap):  # 绘制几何图形
    global size
    turtle.color(color)  # 设置画笔颜色
    turtle.fillcolor(color)  # 设置图形填充颜色
    turtle.begin_fill()  # 开始填充
    turtle.circle(radius, extend)  # 顺时针绘制一段半径为radius像素、角度为extend度的圆弧
    turtle.left(90)
    turtle.forward(gap)
    turtle.right(90)
    turtle.circle(radius - 20, -extend)  # 逆时针绘制一段半径为radius像素、角度为extend度的圆弧
    turtle.end_fill()  # 结束填充
    size -= gap


size = 400
angle = -180
distance = 20
turtle.setup(1200, 600)  # 创建图形窗口
move(-size, int(-size * 0.5))
turtle.speed(10)  # 设置画笔移动的速度为10
turtle.seth(-90)  # 画笔向下
draw('red', size, angle, distance)
draw('orange', size, angle, distance)
draw('yellow', size, angle, distance)
draw('green', size, angle, distance)
draw('cyan', size, angle, distance)
draw('blue', size, angle, distance)
draw('purple', size, angle, distance)
turtle.hideturtle()  # 隐藏画笔箭头
turtle.done()  # 结束绘制
