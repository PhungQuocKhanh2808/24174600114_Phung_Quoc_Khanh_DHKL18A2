#Toán tử tính toán
#Phép cộng
1 + 1
#Phép trừ
2 - 3
#Phép nhân
3 * 4
#Phép chia
5 / 6

1 + 4 * 5 - 2 - 3 / 6
#Dấu ngoặc tròn
(1 + 4) * (5 - 2 - 3) / 6

#Dấu mũ
4 ** 2
4 ** (-2)
4 ** (1/2)

#Phép chia lấy dư
6 % 5
#Phép chia lấy nguyên
6 // 5

#Cho 3 số a,b,c bất kỳ. Tính giá trị trung bình của 3 số này
#B1:Nhập vào 3 giá trị a,b,c
#B2:Tính tổng của 3 số này
#B3:Tính trung bình 3 số
#B4:Xuất ra màn hình kết quả
a = float(input("Nhap vao so a: "))
b = float(input("Nhap vao so b: "))
c = float(input("Nhap vao so c: "))
trung_binh_cong = (a + b + c) / 3
print(f"Trung binh cong cua 3 so {a}, {b}, {c} la {trung_binh_cong:.3f}")

#toán tử so sánh
a > b
a < b
a >= b
a <= b
a == b
a != b
# luôn trả về kết quả boolean (True, False)
