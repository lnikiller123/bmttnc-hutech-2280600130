def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]   # Dòng này phải thụt lề 4 dấu cách so với 'def'
    last_element = tuple_data[-1]    # Dòng này phải thụt lề 4 dấu cách so với 'def'
    return first_element, last_element # Dòng này phải thụt lề 4 dấu cách so với 'def'

# Nhập tuple từ người dùng
input_tuple = input("Nhập tuple, ví dụ (1, 2, 3): ")
first, last = truy_cap_phan_tu(input_tuple)

# In kết quả
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)