import math

class PhanSo:
    def __init__(self, tu =0, mau =1):
        self.tu = tu
        self.mau = mau
    
    def __str__(self) -> str:
        return "{}/{}".format(self.tu, self.mau)
    
    @staticmethod
    def UCLN(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def rutGon(self) -> None:
        ucln = self.UCLN(self.tu, self.mau)
        self.tu /= ucln
        self.mau /= ucln

    def __add__(self, other):
        kq = PhanSo()
        kq.tu = self.tu *other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu *other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __truediv__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.mau
        kq.mau = self.mau * other.tu
        kq.rutGon()
        return kq
    
a = PhanSo()
a.tu = 2
a.mau = 3
b = PhanSo(3, 5)
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")