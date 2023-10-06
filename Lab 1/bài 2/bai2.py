def tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):
    dien_tich = chieu_dai * chieu_rong
    return dien_tich

# Sử dụng hàm
chieu_dai = 10
chieu_rong = 5
dien_tich = tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong)
print(f"Diện tích hình chữ nhật có chiều dài {chieu_dai} và chiều rộng {chieu_rong} là: {dien_tich}")
