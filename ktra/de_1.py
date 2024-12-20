danh_sach_hang_hoa = []

def them_mat_hang():
    try:
        ma_hang = input("Nhập mã hàng: ")
        ten_hang = input("Nhập tên hàng: ")
        don_vi_tinh = input("Nhập đơn vị tính: ")
        don_gia = float(input("Nhập đơn giá: "))
        so_luong = int(input("Nhập số lượng: "))
        thanh_tien = don_gia * so_luong
        vat = thanh_tien * 0.1

        mat_hang = {
            "ma_hang": ma_hang,
            "ten_hang": ten_hang,
            "don_vi_tinh": don_vi_tinh,
            "don_gia": don_gia,
            "so_luong": so_luong,
            "thanh_tien": thanh_tien,
            "vat": vat,
        }
        danh_sach_hang_hoa.append(mat_hang)
        print("Thêm mặt hàng thành công.")
    except ValueError as e:
        print(f"Lỗi nhập liệu: {e}")


def hien_thi_danh_sach():
    if not danh_sach_hang_hoa:
        print("Danh sách mặt hàng trống.")
        return

    print("\nDanh sách mặt hàng:")
    for mat_hang in danh_sach_hang_hoa:
        print(f"Mã hàng: {mat_hang['ma_hang']}, Tên hàng: {mat_hang['ten_hang']}, "
            f"Đơn vị tính: {mat_hang['don_vi_tinh']}, Đơn giá: {mat_hang['don_gia']}, "
            f"Số lượng: {mat_hang['so_luong']}, Thành tiền: {mat_hang['thanh_tien']}, "
            f"VAT: {mat_hang['vat']}")


def tim_kiem_theo_ma(ma_hang):
    for mat_hang in danh_sach_hang_hoa:
        if mat_hang["ma_hang"] == ma_hang:
            return mat_hang
    return None


def xoa_mat_hang():
    try:
        ma_hang = input("Nhập mã hàng cần xóa: ")
        mat_hang = tim_kiem_theo_ma(ma_hang)
        if mat_hang:
            danh_sach_hang_hoa.remove(mat_hang)
            print(f"Đã xóa mặt hàng: {mat_hang['ten_hang']}")
        else:
            raise Exception("Không tìm thấy mặt hàng với mã đã nhập.")
    except Exception as e:
        print(e)


def sua_mat_hang():
    try:
        ma_hang = input("Nhập mã hàng cần sửa: ")
        mat_hang = tim_kiem_theo_ma(ma_hang)
        if mat_hang:
            print("Nhập thông tin mới (bỏ trống nếu không muốn thay đổi):")
            ten_hang = input(f"Tên hàng ({mat_hang['ten_hang']}): ") or mat_hang["ten_hang"]
            don_vi_tinh = input(f"Đơn vị tính ({mat_hang['don_vi_tinh']}): ") or mat_hang["don_vi_tinh"]
            don_gia = input(f"Đơn giá ({mat_hang['don_gia']}): ")
            so_luong = input(f"Số lượng ({mat_hang['so_luong']}): ")

            mat_hang["ten_hang"] = ten_hang
            mat_hang["don_vi_tinh"] = don_vi_tinh
            mat_hang["don_gia"] = float(don_gia) if don_gia else mat_hang["don_gia"]
            mat_hang["so_luong"] = int(so_luong) if so_luong else mat_hang["so_luong"]
            mat_hang["thanh_tien"] = mat_hang["don_gia"] * mat_hang["so_luong"]
            mat_hang["vat"] = mat_hang["thanh_tien"] * 0.1
            print("Thông tin mặt hàng đã được cập nhật.")
        else:
            raise Exception("Không tìm thấy mặt hàng với mã đã nhập.")
    except Exception as e:
        print(e)


def sap_xep_theo_ten():
    danh_sach_hang_hoa.sort(key=lambda x: x["ten_hang"])
    print("Danh sách đã được sắp xếp theo tên.")


while True:
    print("\n1. Xem danh sách mặt hàng")
    print("2. Thêm mặt hàng")
    print("3. Tính toán (đã tích hợp)")
    print("4. Tìm kiếm và xóa mặt hàng")
    print("5. Tìm kiếm và sửa mặt hàng")
    print("6. Sắp xếp danh sách theo tên")
    print("0. Thoát")

    try:
        lua_chon = int(input("Nhập lựa chọn: "))
        if lua_chon == 1:
            hien_thi_danh_sach()
        elif lua_chon == 2:
            them_mat_hang()
        elif lua_chon == 4:
            xoa_mat_hang()
        elif lua_chon == 5:
            sua_mat_hang()
        elif lua_chon == 6:
            sap_xep_theo_ten()
        elif lua_chon == 0:
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")
    except Exception as e:
        print(f"Lỗi: {e}")
