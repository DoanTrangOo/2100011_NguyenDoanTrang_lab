import math

def tong_can_bac_hai_cua_n_so_nguyen_dau_tien(n):
    if n <= 0:
        return 0.0
    total = 0.0
    for i in range(1, n + 1):
        total += math.sqrt(i)
    return total

# Sử dụng hàm để tính tổng căn bậc 2 của n số nguyên đầu tiên
n = 5  # Thay đổi giá trị n tùy ý
result = tong_can_bac_hai_cua_n_so_nguyen_dau_tien(n)
print(f"Tổng căn bậc 2 của {n} số nguyên đầu tiên là: {result}")
