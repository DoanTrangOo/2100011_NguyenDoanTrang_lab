def tinh_toan(a, b):
    # a + b
    tong = a + b
    
    # a / b (kiểm tra b để tránh chia cho 0)
    if b != 0:
        chia = a / b
    else:
        chia = "Không thể chia cho 0"
    
    # a ^ b
    luy_thua = a ** b
    
    return tong, chia, luy_thua

# Sử dụng hàm
a = 5
b = 2
ket_qua = tinh_toan(a, b)

print(f"Tổng của {a} và {b} là: {ket_qua[0]}")
print(f"{a} chia cho {b} là: {ket_qua[1]}")
print(f"{a} ^ {b} là: {ket_qua[2]}")
