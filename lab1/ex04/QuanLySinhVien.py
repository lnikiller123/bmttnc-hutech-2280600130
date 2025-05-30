from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxID = 1
        if (self.soluongSinhVien() > 0):
            maxID = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxID < sv._id):
                    maxID = sv._id
            maxID = maxID + 1
        return maxID

    def soluongSinhVien(self):
        return len(self.listSinhVien) # Using len() for clarity

    def nhapSinhVien(self):
        svid = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        # Added a loop for valid float input
        while True:
            try:
                diemTB = float(input("Nhap diem cua sinh vien: "))
                break
            except ValueError:
                print("Diem khong hop le. Vui long nhap lai so thap phan.")
        sv = SinhVien(svid, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if (sv is not None): # Changed '!=' to 'is not' for comparison with None
            name = input("Nhap ten sinh vien moi: ") # Added "moi" for clarity
            sex = input("Nhap gioi tinh sinh vien moi: ")
            major = input("Nhap chuyen nganh cua sinh vien moi: ")
            # Added a loop for valid float input
            while True:
                try:
                    diemTB = float(input("Nhap diem cua sinh vien moi: "))
                    break
                except ValueError:
                    print("Diem khong hop le. Vui long nhap lai so thap phan.")

            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
            print("Cap nhat thong tin sinh vien thanh cong!")
        else:
            print(f"Sinh vien co ID={ID} khong ton tai.") # Using f-string for better formatting

    def sortByIDC(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
        print("Danh sach sinh vien da duoc sap xep theo ID.")

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        print("Danh sach sinh vien da duoc sap xep theo ten.")

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
        print("Danh sach sinh vien da duoc sap xep theo diem trung binh.")

    def findByID(self, ID):
        searchResult = None
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
                    break # Stop once found
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    def deleteByID(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv is not None): # Changed '!=' to 'is not' for comparison with None
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if (len(listSV) > 0): # Using len() for clarity
            for sv in listSV:
                print(f"{sv._id:<8} {sv._name:<18} {sv._sex:<8} {sv._major:<8} {sv._diemTB:<8.2f} {sv._hocLuc:<8}")
        else:
            print("Khong co sinh vien nao trong danh sach de hien thi.") # More informative message

    def getListSinhVien(self):
        return self.listSinhVien