# Reyhan Putra Adiyatama
# 065002600008

# Fungsi mengecek bilangan prima
def cek_prima(angka):
    if angka <= 1:
        return False
    for i in range(2, angka):
        if angka % i == 0:
            return False
    return True

# Fungsi untuk menampilkan hasil
def tampilkan_hasil(angka):
    if cek_prima(angka):
        print(angka, "adalah bilangan Prima")
    else:
        print(angka, "bukanlah bilangan Prima")

# Program utama
angka = int(input("Masukkan angka: "))
tampilkan_hasil(angka)
