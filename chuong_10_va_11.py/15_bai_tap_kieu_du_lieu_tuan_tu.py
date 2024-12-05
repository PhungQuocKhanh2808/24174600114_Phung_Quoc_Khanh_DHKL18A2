#Bài 1: Nhập vào số nguyên dương n. 
#In ra màn hình dãy số các số nguyên tố nhỏ hơn n theo thứ tự từ nhỏ đến lớn
#Bài làm
ds_nguyen_to = []
while True:
    n = input("Nhap vao so nguyen duong n: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(1, n):
    if i == 1:
        ds_nguyen_to.append(i)
        continue
    for j in range(1,i):
        if i%j == 0 and j != 1 and i != j:
            break
    else:
        ds_nguyen_to.append(i)

ds_nguyen_to.sort()
print(ds_nguyen_to)
# #Tính tổng các giá trị trong danh sách
# tong = sum(ds_nguyen_to)
# print(tong)



#Bài 2: Nhập vào dãy A gồm n phần tử từ bàn phím. 
#Tính tổng các phần tử trong dãy A
ds_so = []
while True:
    n = input("Nhap vao so phan tu n trong danh sach: ")
    if n.isdigit() == False:
        print("Yeu cau nhap lai so nguyen duong!!")
    else:
        n = int(n)
        break

for i in range(n):
    while True:
        so = input(f"Nhap gia tri so thu {i + 1}: ")
        if so.isdigit() == False:
            print("Yeu cau nhap vao so!!")
        else:
            so = float(so)
            break
    ds_so.append(so)

tong = sum(ds_so)
print(f"Tong cac so vua nhap: {tong}")

#suabai
ds_so = []
while True:
    n = input("Nhap vao so phan tu n trong danh sach: ")
    if n.isdigit():  
        n = int(n)
        break
    else:
        print("Yeu cau nhap lai so nguyen!")

for i in range(n):
    while True:
        so = input(f"Nhap gia tri so thu {i + 1}: ")
        if so.isdigit(): 
            so = float(so)
            break
        else:
            print("Yeu cau nhap vao so!")
    ds_so.append(so)

tong = sum(ds_so)
print(f"Tong cac so vua nhap: {tong}")

#Bài 3: Nhập vào số nguyên dương n.
#In ra màn hình: 
# - Danh sách A gồm các số lẻ nhỏ hơn n
# - Danh sách B gồm các số chẵn nhỏ hơn n
#Sắp xếp dãy số theo thứ tự giảm dần
# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

so_le = []
so_chan = []

for i in range(1, n):
    if i % 2 == 0:
        so_chan.append(i)
    else:
        so_le.append(i)

so_le.sort(reverse=True)
so_chan.sort(reverse=True)

print("Danh sách các số lẻ giảm dần:", so_le)
print("Danh sách các số chẵn giảm dần:", so_chan)

#Bai 6

m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

ma_tran = []
for i in range(m):
    row = []
    for j in range(n):
    
        x = int(input(f"Nhập phần tử tại hàng {i+1}, cột {j+1}: "))
        row.append(x)
    ma_tran.append(row)

for i in range(m):
    for j in range(n):
        print(ma_tran[i][j], end=" ")
    print()  

#Bai 8
# Nhập kích thước ma trận và các phần tử của ma trận A
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

ma_tran = []
for i in range(m):
    row = []
    for j in range(n):
        x = int(input(f"Nhập phần tử tại hàng {i+1}, cột {j+1}: "))
        row.append(x)
    ma_tran.append(row)

i = int(input("Nhập cột thứ nhất cần đảo: ")) - 1
j = int(input("Nhập cột thứ hai cần đảo: ")) - 1

for k in range(m):
    ma_tran[k][i], ma_tran[k][j] = ma_tran[k][j], ma_tran[k][i]

print("Ma trận sau khi đảo:")
for row in ma_tran:
    for element in row:
        print(element, end=" ")
    print()

#Bai 11\
print("Tên\tĐiểm")
for ten, diem in "sinh_vien":
    print(f"{ten}\t{diem}")

#Bai 12
ten_xoa = input("Nhập tên sinh viên cần xóa: ")
for i in range(len("sinh_vien")):
    if "sinh_vien"[i][0] == ten_xoa:
        del "sinh_vien"[i]
        print("Đã xóa sinh viên")
        break
else:
    print("Không tìm thấy sinh viên cần xóa")

#Bai 13
ten_moi = input("Nhập tên sinh viên mới: ")
diem_moi = float(input("Nhập điểm của sinh viên mới: "))

ton_tai = False
for ten, diem in "sinh_vien":
    if ten == ten_moi:
        ton_tai = True
        break

if ton_tai:
    print("Thông tin sinh viên đã tồn tại")
else:
    "sinh_vien".append((ten_moi, diem_moi))
    print("Đã thêm sinh viên")