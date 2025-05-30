from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        # Khởi tạo thuộc tính alphabet của lớp CaesarCipher
        # self.alphabet sẽ chứa bảng chữ cái được nhập từ ALPHABET
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        # Lấy độ dài của bảng chữ cái để thực hiện phép toán modulo
        alphabet_len = len(self.alphabet)
        # Chuyển đổi văn bản đầu vào thành chữ in hoa để đảm bảo tính nhất quán
        text = text.upper()
        # Tạo một danh sách rỗng để lưu trữ các ký tự đã mã hóa
        encrypted_text = []

        # Lặp qua từng ký tự trong văn bản
        for letter in text:
            # Tìm chỉ số của ký tự trong bảng chữ cái
            # Nếu ký tự không có trong bảng chữ cái, nó sẽ gây lỗi ValueError
            # Bạn có thể thêm xử lý lỗi ở đây nếu cần
            letter_index = self.alphabet.index(letter)
            # Tính toán chỉ số đầu ra bằng cách dịch chuyển chỉ số gốc và áp dụng modulo
            output_index = (letter_index + key) % alphabet_len
            # Lấy ký tự đã mã hóa từ bảng chữ cái bằng chỉ số đầu ra
            output_letter = self.alphabet[output_index]
            # Thêm ký tự đã mã hóa vào danh sách
            encrypted_text.append(output_letter)
        
        # Nối các ký tự trong danh sách đã mã hóa thành một chuỗi và trả về
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        # Lấy độ dài của bảng chữ cái
        alphabet_len = len(self.alphabet)
        # Chuyển đổi văn bản đầu vào thành chữ in hoa
        text = text.upper()
        # Tạo một danh sách rỗng để lưu trữ các ký tự đã giải mã
        decrypted_text = []

        # Lặp qua từng ký tự trong văn bản
        for letter in text:
            # Tìm chỉ số của ký tự trong bảng chữ cái
            letter_index = self.alphabet.index(letter)
            # Tính toán chỉ số đầu ra bằng cách dịch chuyển ngược chỉ số gốc và áp dụng modulo
            output_index = (letter_index - key) % alphabet_len
            # Lấy ký tự đã giải mã từ bảng chữ cái bằng chỉ số đầu ra
            output_letter = self.alphabet[output_index]
            # Thêm ký tự đã giải mã vào danh sách
            decrypted_text.append(output_letter)
        
        # Nối các ký tự trong danh sách đã giải mã thành một chuỗi và trả về
        return "".join(decrypted_text)