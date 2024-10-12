class debitur:
    def __init__(self, nama, ktp, limit):
        self.nama = nama
        self.__ktp = ktp
        self._limit = limit

    def display(self):
        print(f"Nama Debitur: {self.nama} dengan No KTP: {self.__ktp} dengan limit pinjaman: {self._limit}")


    def tambah_debitur(self):
        self.__ktp = ktp
        self._limit = limit
        self.nama = nama

def cari_debitur(nama_dicari, daftar_debitur):
    for debitur in daftar_debitur:
        if debitur.nama.lower() == nama_dicari.lower():  
            return debitur
    return None 


class pinjaman:
    def __init__(self, nama, ktp, limit, pinjaman=0, bunga=0, bulan=0, angsuran=0):
        self.nama = nama
        self.__ktp = ktp
        self._limit = limit
        self.pinjaman = pinjaman
        self.bunga = bunga
        self.bulan = bulan
        self.angsuran = angsuran
    
    def display(self):        
        angsuran_pokok = self.pinjaman * (self.bunga / 100)
        angsuran_bulanan = angsuran_pokok / self.bulan
        total_angsuran = angsuran_pokok + angsuran_bulanan
        print(f"Nama Debitur: {self.nama}")
        print(f"Pinjaman: {self.pinjaman}, Bunga: {self.bunga}%")
        print(f"Bulan: {self.bulan}, Angsuran Bulanan: {angsuran_bulanan:.2f}")
        print(f"Total Angsuran: {total_angsuran:.2f}")

    def tambah_pinjaman(self):
        nama = input("Masukkan nama debitur: ")
        for debitur in tampil_debitur:
            if debitur.nama == nama:
                nominal_pinjaman = int(input("Masukkan nominal yang ingin dipinjam: "))
                if nominal_pinjaman <= debitur._limit:
                    bunga = int(input("Masukkan bunga (%): "))
                    bulan = int(input("Masukkan jumlah bulan: "))
                    pinjaman_baru = pinjaman(nama, debitur._debitur__ktp, debitur._limit, nominal_pinjaman, bunga, bulan)
                    list_pinjaman.append(pinjaman_baru)
                    print("Pinjaman berhasil ditambahkan")
                    return  
                else:
                    print("Pinjaman melebihi limit")
                    return  
        else:
            print("Debitur dengan nama tersebut tidak ditemukan")

tampil_debitur=[
    debitur("Rahmad", 123, 10000000),
    debitur("Yoyo", 321, 10000000),
    debitur("Yiyi", 100, 10000000),
]
    
list_pinjaman = [] 

while True:
    print("Aplikasi Pinjaman Online")
    print("1. KELOLA DEBITUR")
    print("2. KELOLA PINJAMAN")
    print("3. KELUAR")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        while True:
            print("KELOLA DEBITUR")
            print("1. TAMPIL DEBITUR")
            print("2. CARI DEBITUR")
            print("3. TAMBAH DEBITUR")
            print("4. KELUAR")
            pilihan2 = input("Pilih menu: ")
            if pilihan2 == "1":
                for debitur in tampil_debitur:
                    debitur.display()

            elif pilihan2 == "2":
                nama_dicari = input("Masukkan nama: ")
                debitur = cari_debitur(nama_dicari, tampil_debitur)  
                if debitur:
                    debitur.display()
                else:
                    print("Debitur dengan nama tersebut tidak ditemukan")

            elif pilihan2 == "3":
                ktp = int(input("Masukkan No KTP: "))
                if any(debitur._debitur__ktp == ktp for debitur in tampil_debitur): 
                    print("Debitur dengan No KTP tersebut sudah ada")
                else:
                    nama = input("Masukkan nama: ")
                    limit = int(input("Masukkan limit: "))
                    debitur_baru = debitur(nama, ktp, limit)
                    tampil_debitur.append(debitur_baru)
                    print("Debitur berhasil ditambahkan")
            elif pilihan2 == "4":
                break
            else:
                print("Pilihan tidak ada")
    elif pilihan == "2":
        while True:
            print("KELOLA PINJAMAN")
            print("1. TAMBAH PINJAMAN")
            print("2. TAMPIL PINJAMAN")
            print("3. KELUAR")
            pilih = input("Pilih menu: ")
            if pilih == "1":
                pinjaman_obj = pinjaman("", 0, 0, 0)
                pinjaman_obj.tambah_pinjaman()
            elif pilih == "2":
                if not list_pinjaman:  
                    print("Belum ada pinjaman yang ditambahkan.")
                else:
                    for pinjaman in list_pinjaman:
                        pinjaman.display()
            elif pilih == "3":
                break
            else:
                print("Pilihan tidak ada")
    elif pilihan == "3":
        print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM,TAPI JANGAN SAMPAI PINJOL BENERAN YAA!!!")
        break
    else:
        print("Pilihan tidak ada")