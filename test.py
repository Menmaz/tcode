import turtle

# Tạo một đối tượng rùa
t = turtle.Turtle()

# Đặt màu nền cho màn hình
turtle.bgcolor("white")

# Đặt màu cho rùa
t.color("green")

# Đặt tốc độ vẽ (1 là chậm nhất, 10 là nhanh nhất)
t.speed(1)

# Vẽ một hình vuông
for _ in range(4):
    t.forward(100)  # Di chuyển về phía trước 100 đơn vị
    t.right(90)  # Rẽ phải 90 độ

# Kết thúc chương trình khi nhấn chuột vào màn hình
turtle.done()
