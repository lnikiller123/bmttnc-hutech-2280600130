from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
# Khởi tạo đối tượng CaesarCipher một lần duy nhất khi ứng dụng bắt đầu
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    # Lấy dữ liệu JSON từ yêu cầu
    data = request.json
    # Trích xuất văn bản gốc và khóa từ dữ liệu
    plain_text = data['plain_text']
    key = int(data['key']) # Chuyển đổi khóa sang số nguyên

    # Mã hóa văn bản sử dụng đối tượng caesar_cipher đã khởi tạo
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    # Trả về kết quả dưới dạng JSON
    return jsonify({'encrypted_message' : encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    # Lấy dữ liệu JSON từ yêu cầu
    data = request.json
    # Trích xuất văn bản đã mã hóa và khóa từ dữ liệu
    cipher_text = data['cipher_text']
    key = int(data['key']) # Chuyển đổi khóa sang số nguyên

    # Giải mã văn bản sử dụng đối tượng caesar_cipher đã khởi tạo
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    # Trả về kết quả dưới dạng JSON
    return jsonify({'decrypted_message': decrypted_text})

# main function
if __name__ == "__main__":
    # Chạy ứng dụng Flask
    # host="0.0.0.0" cho phép truy cập từ mọi địa chỉ IP
    # port=5000 là cổng mặc định
    # debug=True cho phép chế độ gỡ lỗi (tự động tải lại khi thay đổi code)
    app.run(host="0.0.0.0", port=5000, debug=True)