def doi_giay_gio_phut_giay(so_giay):
    gio = so_giay // 3600
    phut = (so_giay % 3600) // 60
    giay = so_giay % 60
    return f"{gio}:{phut}:{giay}"

# Sử dụng hàm để đổi giây thành giờ, phút và giây
so_giay = 3770
ket_qua = doi_giay_gio_phut_giay(so_giay)
print(ket_qua)
