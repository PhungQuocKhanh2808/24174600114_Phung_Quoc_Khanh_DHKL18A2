#Bai 1: 
r = float(input("Nhap vao ban kinh: "))
h = float(input("Nhap vao chieu cao: "))
if h > 0 and r > 0:
    pi = 3.14
    dtxq = 2*pi*r*h
    dttp = dtxq + 2*pi*r**2
    print(f"Dien tich xung quanh: {dtxq:.2f}")
    print(f"Dien tich toan phan: {dttp:.2f}")
else:
    print("gia tri nhap khong thoa man")

print("ket thuc chuong trinh")


#Bai 2
import math
x = float(input("nhap gia tri bieu thuc x: "))
if x >= 0 and x != 0:
    print("gia tri khong duoc am hoac bang 0")
else:
    print("gia tri khong thoa man")    
f_x = (-x + (x**2 + 4)**(1/2)/(x**4 + 1)**(1/7))
x = float(input("nhap gia tri cua x: "))
f_x = (-x + (x**2 + 4)**(1/2)/(x**4 + 1)**(1/7))
print(f"Gia tri cua f(x) = {f_x:.2f}")
print("ket thuc chuong trinh")
