from tabulate import tabulate
class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat
        self.absen_status = False

    
    def absen(self):
        if not self.absen_status:
            self.absen_status = True
            print(f"{self.nama} telah absen.")
        else:
            print(f"{self.nama} sudah absen sebelumnya.")
    
    @staticmethod  
    def lihat(pegawai_list):  
        headers = ["Nama Pegawai", "NIK", "Alamat", "Keterangan"]
        table = []
        for pegawai in pegawai_list:  
            keterangan = "Hadir" if pegawai.absen_status else "Belum Hadir"
            table.append([pegawai.nama, pegawai.nik, pegawai.alamat, keterangan])  
        print(tabulate(table, headers, tablefmt="grid"))

class Produk:
    _produk_counter = 0
    def __init__(self,nama_produk, jenis_produk,harga):
        Produk._produk_counter += 1
        self.kode_produk = f"P{Produk._produk_counter:03d}"
        self.nama = nama_produk
        self.jenis = jenis_produk
        self.harga = harga

    def info_produk(self):
        return [self.kode_produk, self.nama, self.jenis, self._harga]
    
    @staticmethod
    def lihat_produk(produk_list):
        headers = ["Kode Produk", "Nama Produk", "Jenis Produk", "Harga"]
        table = [[produk.kode_produk, produk.nama, produk.jenis, produk.harga] for produk in produk_list]
        print(tabulate(table, headers, tablefmt="grid"))
    
class Snack(Produk):
    def __init__(self, nama_produk, harga):
        super().__init__(nama_produk, 'Snack', harga)

class Makanan(Produk):
    def __init__(self, nama_produk, harga):
        super().__init__(nama_produk, 'Makanan', harga)

class Minuman(Produk):
    def __init__(self, nama_produk, harga):
        super().__init__(nama_produk, 'Minuman', harga)



class Transaksi:
    _transaksi_counter = 0
    def __init__(self, pegawai):
        Transaksi._transaksi_counter += 1
        self.no_transaksi = f"T{Transaksi._transaksi_counter:03d}"  
        self.pegawai = pegawai
        self.detail_transaksi = []

    
    def tambah_produk(self, produk, jumlah):
        self.detail_transaksi.append([produk, jumlah])
    
    
    def lihat_transaksi(self):
        headers = ["Kode Produk", "Nama Produk", "Jenis Produk", "Harga", "Jumlah"]
        table = [[item[0].kode_produk, item[0].nama, item[0].jenis, item[0].harga, item[1]] for item in self.detail_transaksi]
        print(f"Transaksi No: {self.no_transaksi}")
        print(f"Pegawai: {self.pegawai.nama} (NIK: {self.pegawai.nik})")
        print(tabulate(table, headers, tablefmt="grid"))

class Struk:
    def __init__(self, transaksi):
        self.transaksi = transaksi

    def lihat_struk(self):
        headers = ["No Transaksi", "Nama Pegawai", "Total Produk", "Total Harga"]
        total_produk = sum([item[1] for item in self.transaksi.detail_transaksi])
        total_harga = sum([item[0].harga * item[1] for item in self.transaksi.detail_transaksi])
        table = [[self.transaksi.no_transaksi, self.transaksi.pegawai.nama, total_produk, total_harga]]
        print(tabulate(table, headers, tablefmt="grid"))

def menu():
    pegawai_list = []
    produk_list = []
    transaksi_list = []
    while True:
        print("=== MENU UTAMA ===")
        print("1. Tambah Pegawai")
        print("2. Absen Pegawai")
        print("3. Lihat Pegawai Hadir")
        print("4. Tambah Produk")
        print("5. Lihat Produk")  
        print("6. Tambah Transaksi")
        print("7. Lihat Transaksi")
        print("8. Lihat Struk")
        print("9. Keluar")  
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            nik = input("Masukkan NIK pegawai: ")
            nama = input("Masukkan nama pegawai: ")
            alamat = input("Masukkan alamat:")
            pegawai = Pegawai(nik, nama, alamat)
            pegawai_list.append(pegawai)
            print("Pegawai berhasil ditambahkan.")
        elif pilihan == "2":
            nik = input("Masukkan NIK Pegawai untuk absen: ")
            for pegawai in pegawai_list:
                if pegawai.nik == nik:
                    pegawai.absen()
                    break
            else:
                print("Pegawai tidak ditemukan.")
        elif pilihan == "3":
            Pegawai.lihat(pegawai_list)
        elif pilihan == "4":
            nama_produk = input("Masukkan Nama Produk: ")
            jenis_produk = input("Masukkan Jenis Produk (Snack, Makanan, Minuman): ")
            harga = float(input("Masukkan Harga: "))

            if jenis_produk.lower() == "snack":
                produk = Snack(nama_produk, harga)
            elif jenis_produk.lower() == "makanan":
                produk = Makanan(nama_produk, harga)
            elif jenis_produk.lower() == "minuman":
                produk = Minuman(nama_produk, harga)
            else:
                print("Jenis produk tidak valid.")
                continue
            produk_list.append(produk)
            print(f"{jenis_produk.capitalize()} berhasil ditambahkan.")
        elif pilihan == "5":  
            if produk_list:
                Produk.lihat_produk(produk_list)
            else:
                print("Tidak ada produk yang tersedia.")
        elif pilihan == "6":
            nik = input("Masukkan NIK Pegawai: ")
            for pegawai in pegawai_list:
                if pegawai.nik == nik:
                    transaksi = Transaksi(pegawai)  
                    while True:
                        kode_produk = input("Masukkan Kode Produk (atau 'selesai' untuk menyelesaikan): ")
                        if kode_produk.lower() == "selesai":
                            break
                        for produk in produk_list:
                            if produk.kode_produk == kode_produk:
                                jumlah = int(input("Masukkan Jumlah Produk: "))
                                transaksi.tambah_produk(produk, jumlah)
                                break
                        else:
                            print("Produk tidak ditemukan.")
                    transaksi_list.append(transaksi)
                    print("Transaksi berhasil ditambahkan.")
                    break
            else:
                print("Pegawai tidak ditemukan.")
        elif pilihan == "7":
            for transaksi in transaksi_list:
                transaksi.lihat_transaksi()
        elif pilihan == "8":
            for transaksi in transaksi_list:
                struk = Struk(transaksi)
                struk.lihat_struk()
        elif pilihan == "9":
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    menu()    