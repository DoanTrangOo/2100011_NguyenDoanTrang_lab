def in_tam_giac_rong_khac(n):
    for i in range(n):
        for j in range(n):
            if i == n - 1 or j == 0 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Sử dụng hàm để in ra tam giác rỗng khác
so_hang = 9  # Thay đổi số hàng tùy ý
in_tam_giac_rong_khac(so_hang)
