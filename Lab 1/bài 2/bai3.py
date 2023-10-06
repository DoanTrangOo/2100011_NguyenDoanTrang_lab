def la_so_nguyen_to(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def xuat_so_nguyen_to_trong_khoang(start, end):
    if start < 2:
        start = 2
    for num in range(start, end + 1):
        if la_so_nguyen_to(num):
            print(num)

# Sử dụng hàm để xuất tất cả số nguyên tố trong khoảng từ 10 đến 50
start = 10
end = 50
print(f"Các số nguyên tố trong khoảng từ {start} đến {end} là:")
xuat_so_nguyen_to_trong_khoang(start, end)
