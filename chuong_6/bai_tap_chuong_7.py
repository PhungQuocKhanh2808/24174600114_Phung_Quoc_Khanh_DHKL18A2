import math

# Nhập bán kính và chiều cao từ bàn phím
r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))

# Định nghĩa giá trị pi
pi = 3.14

# Tính diện tích xung quanh
dien_tich_xung_quanh = 2 * pi * r * h

# Tính diện tích toàn phần
dien_tich_toan_phan = 2 * pi * r * (r + h)

# Tính thể tích
the_tich = pi * r ** 2 * h

# Làm tròn đến số thập phân thứ hai
dien_tich_xung_quanh = round(dien_tich_xung_quanh, 2)
dien_tich_toan_phan = round(dien_tich_toan_phan, 2)
the_tich = round(the_tich, 2)

# In kết quả
print(f"Diện tích xung quanh của khối trụ: {dien_tich_xung_quanh}")
print(f"Diện tích toàn phần của khối trụ: {dien_tich_toan_phan}")
print(f"Thể tích của khối trụ: {the_tich}")

# bai 2 
#tu so = -x + (x**2 + 4)**(1/2)
#mau so = (x**4 + 1)**(1/7)
f_x = (-x + (x**2 + 4)**(1/2)/(x**4 + 1)**(1/7))
x = float(input("nhap gia tri cua x: "))
f_x = (-x + (x**2 + 4)**(1/2)/(x**4 + 1)**(1/7))
print(f"Gia tri cua f(x) = {f_x:.2f}")


