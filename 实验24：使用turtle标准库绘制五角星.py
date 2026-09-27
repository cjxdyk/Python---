import turtle as t
t.pensize(5) # 设置画笔粗细
t.pencolor("yellow") # 设置画笔颜色
t.fillcolor("red") # 设置填充颜色
t.begin_fill() # 绘制带填充的包围开始
for _ in range(5):
    t.forward(200) # 向前绘制200像素
    t.right(144) # 右偏转144度
t.end_fill() # 绘制带填充的包围结束
t.penup() # 提起画笔
t.goto(-150, -120) # 移动
# 签上自己的名字
t.pencolor("black") # 设置画笔颜色
t.write("作者:张三", font=('Arial', 21, 'normal')) # 写文本
t.mainloop() # 主函数循环,不关闭画板
