# Reyhan Putra Adiyatama
# 065002600008

# Write File
nama = input("Masukkan Nama mu: ")
umur = input("Masukkan Umur mu: ")
alamat = input("Masukkan Alamatmu: ")
email = input("Masukkan Emailmu: ")
dosen_wali = input("Masukkan Dosen Walimu: ")

file = open("Biodata.txt", "w")
file.write("Nama: " + nama + "\n")
file.write("Umur: " + umur + " Tahun\n")
file.write("Alamat: " + alamat + "\n")
file.write("Email: " + email + "\n")
file.write("Dosen Wali: " + dosen_wali)
file.close()

# Read File
file = open("Biodata.txt", "r")
text = file.read()
print("\nBerikut Ini Data Kamu")
print(text)
file.close()
