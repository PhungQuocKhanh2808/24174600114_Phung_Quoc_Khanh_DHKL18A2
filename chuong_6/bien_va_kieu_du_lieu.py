#Khai báo biến
a = 1
b = 1
#Khi đặt tên phải tuân thủ các quy tắc sau
# - Sử dụng chữ viết thường không dấu
# - Sử dụng dấu _ thay cho khoảng cách giữa 2 chữ
# - Sử dụng chữ viết hoa chỉ khi muốn nhấn mạnh giá trị biến không được phép thay đổi (VD: POST_TIME = 1)
# - Không được đặt tên trùng với các biến đã được khai báo hoặc các câu lệnh có sẵn trong Python
# - Không được đặt tên bắt đầu bằng các số hoặc đặt tên chứa các kí tự đặc biệt
# - Đặt tên phải có ý nghĩa

#Đặt tên biến đúng:
di_hoc = 1
DI_HOC = 2

#Đặt tên biến sai
# biến = 1
# if = 1
# else = 2
# print = 1
# 123Abv = 2
# a%2&2]as = 1

#Kiểu dữ liệu:
#Trong python kiểu dữ liệu của một biến chỉ được xác định khi biến đó được gán giá trị
bien_int = 3 #Định dạng int (integer) - kiểu số nguyên: ...-2, -1, 0, 1, 2,...
bien_float = 4.678 #Định dạng float - kiểu số thực: ....-2.4, -2.324,...,0, 1.0, 1.1
bien_string = "Day la kieu ky tu" #Định dạng str (string) - kiểu ký tự: abcdef....

kieu_boolean_1 = True   #Định dạng bool (Boolean) - kiểu lựa chọn True, False 
kieu_boolean_2 = False
#0 -> False
#1 -> True

kieu_none = None  #Định dạng khai báo không định dạng

kieu_list = [1,2,"abc"] #Định dạng list (danh sách) - kiểu dữ liệu tuần tự danh sách: [1,"abc", 4.6]
kieu_dictionary = {"khoa": "gia tri", "a": 1} #Định dạng kiểu dict (từ điển) - kiểu dữ liệu tuần tự từ điển
kieu_tuple  = (1,2,"abc") # Định dạng tuple - kiểu dữ liệu tuần tự tuple
kieu_set = {1,2,"abc"} # Định dạng set (tập hợp) - kiểu dữ liệu tuần tự tập hợp


#Kiểm tra kiểu dữ liệu của một biến bất kì
print(type(bien_float))
#Biến là một kho lưu trữ dữ liệu