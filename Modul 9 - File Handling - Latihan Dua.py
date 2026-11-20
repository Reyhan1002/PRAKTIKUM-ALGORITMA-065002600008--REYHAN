# Reyhan Putra Adiyatama
# 065002600008

def buat_file():
    nama_file = input("Masukkan Nama File: ")
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM kamu: ")
    angkatan = input("Masukkan Tahun Angkatanmu: ")

    file = open(nama_file + ".txt", "w")
    file.write("Nama: " + nama + "\n")
    file.write("NIM: " + nim + "\n")
    file.write("Angkatan: " + angkatan + "\n")
    file.close()

    print("\nFile Berhasil Dibuat")


def baca_file():
    nama_file = input("Masukkan Nama File: ")

    file = open(nama_file + ".txt", "r")
    text = file.read()
    print("\n" + text)
    file.close()


def tambah_file():
    nama_file = input("Masukkan Nama File: ")
    nama_sahabat = input("Masukkan Nama Sahabatmu: ")
    catatan = input("Masukkan Catatan Tambahan kamu: ")

    file = open(nama_file + ".txt", "a")
    file.write("Nama Sahabat: " + nama_sahabat + "\n")
    file.write("Catatan: " + catatan + "\n")
    file.close()

    print("\nData Berhasil Ditambahkan")


while True:
    print("\n===== Program File Handling =====")
    print("1. Membuat dan Menulis File")
    print("2. Membaca File")
    print("3. Menambahkan Text Pada File")
    print("4. Keluar Dari Program")

    pilihan = input("\nMasukkan Pilihan Berupa Angka (1/2/3/4): ")

    if pilihan == "1":
        buat_file()

    elif pilihan == "2":
        baca_file()

    elif pilihan == "3":
        tambah_file()

    elif pilihan == "4":
        print("Terima Kasih Sudah Menggunakan Program Saya")
        break

    else:
        print("Pilihan Tidak Valid!")
