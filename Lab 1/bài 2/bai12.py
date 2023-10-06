# a) Xuất tất cả các số lẻ không chia hết cho 5
def so_le_khong_chia_het_cho_5(arr):
    ket_qua = [x for x in arr if x % 2 != 0 and x % 5 != 0]
    return ket_qua
# b) Xuất tất cả các số Fibonacci
def so_fibonacci(n):
    a, b = 0, 1
    fibonacci = []
    while b <= n:
        fibonacci.append(b)
        a, b = b, a + b
    return fibonacci
# c) Tìm số nguyên tố lớn nhất
def so_nguyen_to_lon_nhat(arr):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [x for x in arr if is_prime(x)]
    if primes:
        return max(primes)
    else:
        return None
