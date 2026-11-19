# Reyhan Putra Adiyatama
# 065002600008
# Fungsi Rekursif

def perpangkatan(base, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / perpangkatan(base, -power)
    else:
        return base * perpangkatan(base, power - 1)


def program():
    print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")

    angka = input("Masukkan Angka: ")

    if angka == "":
        print("Program Selesai")
        return

    pangkat = int(input("Masukkan Pangkatnya: "))

    hasil = perpangkatan(int(angka), pangkat)

    print("Hasilnya adalah:", hasil)
    print()

    program()


program()
