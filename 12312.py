import turtle

# 화면 설정
wn = turtle.Screen()
wn.bgcolor("white")

# 거북이 설정
t = turtle.Turtle()
t.speed(1)  # 거북이 속도 조절

# 머리 그리기
t.penup()
t.goto(0, -100)
t.pendown()
t.begin_fill()
t.color("peachpuff")
t.circle(100)
t.end_fill()

# 눈 그리기 (왼쪽 눈)
t.penup()
t.goto(-30, 20)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(20)
t.end_fill()

# 눈 그리기 (오른쪽 눈)
t.penup()
t.goto(30, 20)
t.pendown()
t.begin_fill()
t.color("white")
t.circle(20)
t.end_fill()

# 눈동자 그리기 (왼쪽 눈동자)
t.penup()
t.goto(-25, 30)
t.pendown()
t.begin_fill()
t.color("black")
t.circle(10)
t.end_fill()

# 눈동자 그리기 (오른쪽 눈동자)
t.penup()
t.goto(35, 30)
t.pendown()
t.begin_fill()
t.color("black")
t.circle(10)
t.end_fill()

# 코 그리기
t.penup()
t.goto(5, 10)
t.pendown()
t.begin_fill()
t.color("rosybrown")
t.setheading(90)
t.forward(20)
t.setheading(0)
t.forward(20)
t.setheading(270)
t.forward(20)
t.end_fill()

# 입 그리기
t.penup()
t.goto(0, -10)
t.pendown()
t.color("red")
t.setheading(270)
t.circle(10, 180)

# 종료
wn.mainloop()

