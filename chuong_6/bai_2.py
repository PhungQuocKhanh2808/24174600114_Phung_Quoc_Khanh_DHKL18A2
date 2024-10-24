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
