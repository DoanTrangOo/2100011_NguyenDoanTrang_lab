import math

def giai_phuong_trinh_bac_hai(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình có vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            x = -c / b
            return f"Nghiệm của phương trình là x = {x}"
    else:
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Nghiệm của phương trình là x1 = {x1} và x2 = {x2}"
        elif delta == 0:
            x = -b / (2*a)
            return f"Nghiệm kép của phương trình là x1 = x2 = {x}"
        else:
            return "Phương trình vô nghiệm"

# Sử dụng hàm để giải phương trình bậc 2
a = 1
b = -3
c = 2

ket_qua = giai_phuong_trinh_bac_hai(a, b, c)
print(ket_qua)
