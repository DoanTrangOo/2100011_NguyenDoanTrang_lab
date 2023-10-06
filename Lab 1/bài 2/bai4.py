def la_so_Fibonacci(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    else:
        a, b = 0, 1
        while b < n:
            a, b = b, a + b
        return b == n

# Sử dụng hàm để kiểm tra xem một số nguyên có phải là số Fibonacci hay không
n = 13  # Thay đổi giá trị n tùy ý
if la_so_Fibonacci(n):
    print(f"{n} là số Fibonacci")
else:
    print(f"{n} không phải là số Fibonacci")
