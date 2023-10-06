def fibonacci_de_quy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

# Sử dụng đệ quy để tìm số Fibonacci thứ n
n = 10  # Thay đổi giá trị n tùy ý
result = fibonacci_de_quy(n)
print(f"Số Fibonacci thứ {n} là: {result}")
