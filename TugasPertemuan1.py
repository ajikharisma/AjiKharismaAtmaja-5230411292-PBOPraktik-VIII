def luas_jajar_genjang():
    alas = float(input("Masukkan panjang: "))
    tinggi = float(input("Masukkan lebar: "))
    return alas*tinggi

def luas_alas_prisma():
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
    return 0.5 * alas * tinggi_segitiga

def volume_prisma():
    luas_alas = luas_alas_prisma()
    tinggi_prisma = float(input("Masukkan tinggi prisma: "))
    return luas_alas * tinggi_prisma

def menu():
    print ("\nPilih operasi yang ingin anda lakukan")
    print ("1.Menghitung luas jajar genjang")
    print ("2.menghitung volume prisma")
    print ("3.Keluar")

while True:
    menu()
    pilih = input("Masukkan No yang ingin anda pilih : ")

    if pilih == "1":
        print("\nMenghitung Luas Jajar Genjang")
        print("Luas Jajar Genjang = ",luas_jajar_genjang(),"\n")
    
    elif pilih == "2":
        print("\nMenghitung Volume Prisma")
        print("Volume Prisma = ",volume_prisma(),"\n")
    
    elif pilih == "3":
        print("\nTerima kasih telah menggunakan program ini")
        break
    
    else:
        print("Pilihan atau inputan anda salah,mohon dicoba lagi")