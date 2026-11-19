# Reyhan Putra Adiyatama
# 065002600008
# Fungsi Rekursif

# Fungsi untuk memasukkan angka
def input_angka(jumlah, urutan=1):
    if urutan > jumlah:
        return 0
    else:
        angka = int(input("Masukkan bilangan ke-" + str(urutan) + ": "))
        return angka + input_angka(jumlah, urutan + 1)

# Program utama
jumlah = int(input("Masukkan Jumlah: "))
hasil = input_angka(jumlah)
print("Hasil dari penjumlahan adalah:", hasil)
