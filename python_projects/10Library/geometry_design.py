import turtle

def move(x=0, y=0):
    """
    画笔悬空移动
    :param x:
    :param y:
    :return:
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

#  初始化
turtle.setup(1000, 500)
turtle.pensize(5)

# 绘制红色三角
move(-350, -50)
turtle.color('red')
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(90, steps=3)
turtle.end_fill()

# 绘制蓝色正方形
move(-180, -50)
turtle.color('dodger blue')
turtle.fillcolor('dodger blue')
turtle.begin_fill()
turtle.circle(80, steps=4)
turtle.end_fill()

# 绘制黄色五边形
move(0, -50)
turtle.color('yellow')
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(80, steps=5)
turtle.end_fill()

# 绘制淡粉色六边形
move(180, -50)
turtle.color('seashell')
turtle.fillcolor('seashell')
turtle.begin_fill()
turtle.circle(80, steps=6)
turtle.end_fill()

# 绘制紫色圆形
move(350, -50)
turtle.color('purple')
turtle.fillcolor('purple')
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

turtle.done ()