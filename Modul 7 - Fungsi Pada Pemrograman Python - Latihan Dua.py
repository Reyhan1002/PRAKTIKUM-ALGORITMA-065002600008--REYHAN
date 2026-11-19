# Reyhan Putra Adiyatama
# 065002600008

def ordinal(angka):
    if angka == 1:
        return (angka, 'st')
    elif angka == 2:
        return (angka, 'nd')
    elif angka == 3:
        return (angka, 'rd')
    else:
        return (angka, 'th')


print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
    angka = int(input("masukkan angka: "))
    hasil = ordinal(angka)
    print(hasil)

    if angka == 0:
        print("terima kasih telah menggunakan program saya")
        break
