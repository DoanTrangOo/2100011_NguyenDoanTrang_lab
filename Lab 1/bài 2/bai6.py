def tong_n_so_fibonacci_de_quy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return tong_n_so_fibonacci_de_quy(n - 1) + fibonacci_de_quy(n)

# Sử dụng đệ quy để tính tổng n số Fibonacci đầu tiên
n = 10  # Thay đổi giá trị n tùy ý
result = tong_n_so_fibonacci_de_quy(n)
print(f"Tổng của {n} số Fibonacci đầu tiên là: {result}")
