from QuanLySinhVien import QuanLySinhVien

def main():
    qlsv = QuanLySinhVien()
    while True:
        print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
        print("********************MENU********************")
        print("*** 1. Them sinh vien.")
        print("*** 2. Cap nhat thong tin sinh vien boi ID.")
        print("*** 3. Xoa sinh vien boi ID.")
        print("*** 4. Tim kiem sinh vien theo ten.")
        print("*** 5. Sap xep sinh vien theo diem trung binh.")
        print("*** 6. Sap xep sinh vien theo ten.") # Changed to reflect sortByName
        print("*** 7. Hien thi danh sach sinh vien.")
        print("*** 0. Thoat")
        print("********************************************")

        try:
            key = int(input("Nhap tuy chon: "))
        except ValueError:
            print("Vui long nhap mot so tu 0 den 7.")
            continue

        if (key == 1):
            print("\n1. Them sinh vien.")
            qlsv.nhapSinhVien()
            print("\nThem sinh vien thanh cong!")
        elif (key == 2):
            if (qlsv.soluongSinhVien() > 0):
                print("\n2. Cap nhat thong tin sinh vien.")
                try:
                    ID = int(input("Nhap ID sinh vien can cap nhat: "))
                    qlsv.updateSinhVien(ID)
                except ValueError:
                    print("ID khong hop le. Vui long nhap mot so nguyen.")
            else:
                print("\nDanh sach sinh vien trong! Khong co sinh vien de cap nhat.")
        elif (key == 3):
            if (qlsv.soluongSinhVien() > 0):
                print("\n3. Xoa sinh vien.")
                try:
                    ID = int(input("Nhap ID sinh vien can xoa: "))
                    if (qlsv.deleteByID(ID)):
                        print(f"\nSinh vien co id = {ID} da bi xoa.")
                    else:
                        print(f"\nSinh vien co id = {ID} khong ton tai.")
                except ValueError:
                    print("ID khong hop le. Vui long nhap mot so nguyen.")
            else:
                print("\nDanh sach sinh vien trong! Khong co sinh vien de xoa.")
        elif (key == 4):
            if (qlsv.soluongSinhVien() > 0):
                print("\n4. Tim kiem sinh vien theo ten.")
                name = input("Nhap ten de tim kiem: ")
                searchResult = qlsv.findByName(name)
                if len(searchResult) > 0:
                    print("\nKet qua tim kiem:")
                    qlsv.showSinhVien(searchResult)
                else:
                    print(f"Khong tim thay sinh vien nao voi ten '{name}'.")
            else:
                print("\nDanh sach sinh vien trong! Khong the tim kiem.")
        elif (key == 5):
            if (qlsv.soluongSinhVien() > 0):
                print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
                qlsv.sortByDiemTB()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sach sinh vien trong! Khong the sap xep.")
        elif (key == 6): # Corrected indentation for this block
            if (qlsv.soluongSinhVien() > 0):
                print("\n6. Sap xep sinh vien theo ten.")
                qlsv.sortByName()
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sach sinh vien trong! Khong the sap xep.")
        elif (key == 7): # Corrected indentation for this block
            if (qlsv.soluongSinhVien() > 0):
                print("\n7. Hien thi danh sach sinh vien.")
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sach sinh vien trong!")
        elif (key == 0): # Corrected indentation for this block
            print("\nBan da chon thoat chuong trinh!")
            break
        else: # Corrected indentation for this block
            print("\nKhong co chuc nang nay!")
            print("\nHay chon chuc nang trong hop menu.")

if __name__ == "__main__":
    main()