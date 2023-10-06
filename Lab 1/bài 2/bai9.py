def tinh_giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * tinh_giai_thua(n - 1)

# Sử dụng hàm để tính n!
n = 5  # Thay đổi giá trị n tùy ý
ket_qua = tinh_giai_thua(n)
print(f"{n}! = {ket_qua}")
