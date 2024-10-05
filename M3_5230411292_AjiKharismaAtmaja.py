class daftar_menu:
    def __init__(self,nama,harga):
        self.nama = nama
        self.harga = harga


    def menu_makanan(self):
        print(f"Nama Makanan: {self.nama} harga: {self.harga}")

    def menu_minuman(self):
        print(f"Nama Minuman: {self.nama} harga: {self.harga}")

while True:
    print("Daftar Menu")
    print("1. Daftar Menu Makanan")
    print("2. Daftar Menu Minuman")
    print("3. Menambahkan Menu Makanan dan Minuman")
    print("4. Keluar")
    pilihan = input("Pilih Menu: ")
    if pilihan == "1":
        menu_makanan = []
        
        menu_makanan.append(daftar_menu("Nasi Goreng", 15000))
        menu_makanan.append(daftar_menu("Mie Goreng", 12000))
        menu_makanan.append(daftar_menu("Gado-Gado", 8000))
        for i in menu_makanan:
            i.menu_makanan()
    elif pilihan == "2":
        print("Daftar Menu Minuman")
        menu_minuman = []
        menu_minuman.append(daftar_menu("Boba", 50000))
        menu_minuman.append(daftar_menu("Jus Jeruk", 20000))
        menu_minuman.append(daftar_menu("Kopi", 15000))
        for i in menu_minuman:
            i.menu_minuman()

    elif pilihan == "3":
        print("Tambah Menu")
        print("1. Tambah Menu Makanan")
        print("2. Tambah Menu Minuman")
        print("3. Kembali")
        tambah = input("Pilih Menu: ")
        if tambah == "1":
            nama = input("Nama Menu: ")
            harga = int(input("Harga Menu: "))
            menu_makanan = daftar_menu(nama,harga)
            print(f"Menu {nama} berhasil ditambahkan")
            menu_makanan.append(daftar_menu)








            

            
        elif tambah == "2":
            nama = input("Nama Menu: ")
            harga = int(input("Harga Menu: "))
            menu_minuman = daftar_menu(nama,harga)
            print(f"Menu {nama} berhasil ditambahkan")
            
        elif tambah == "3":
            continue
        else:
            print("Pilihan tidak tersedia")
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak tersedia")

    
    
