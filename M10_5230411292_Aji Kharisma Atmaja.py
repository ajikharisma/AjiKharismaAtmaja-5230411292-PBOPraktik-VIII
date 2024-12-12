import mysql.connector
from mysql.connector import Error
from datetime import datetime
from tabulate import tabulate

class penjualan:
    def __init__(self, host="localhost", user="root", password="", database="penjualan"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cur = self.conn.cursor()

    # Fungsi untuk membuat database
    def create_database(self):
        try:
            self.cur.execute("CREATE DATABASE penjualan")
            print("Database 'penjualan' berhasil dibuat.")
        except mysql.connector.Error as e:
            print(f"Terjadi kesalahan saat membuat database: {e}")

    # Fungsi untuk membuat tabel Pegawai
    def create_pegawai_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE Pegawai (
                    NIK CHAR(50) NOT NULL PRIMARY KEY,
                    Nama_Pegawai VARCHAR(15),
                    Alamat VARCHAR(255)
                )
            """)
            print("Tabel 'Pegawai' berhasil dibuat.")
        except mysql.connector.Error as e:
            print(f"Terjadi kesalahan saat membuat tabel Pegawai: {e}")

    # Fungsi untuk membuat tabel Transaksi
    def create_transaksi_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE Transaksi (
                    No_Transaksi CHAR(4) NOT NULL PRIMARY KEY,
                    Detail_Transaksi VARCHAR(255)
                )
            """)
            print("Tabel 'Transaksi' berhasil dibuat.")
        except mysql.connector.Error as e:
            print(f"Terjadi kesalahan saat membuat tabel Transaksi: {e}")

    # Fungsi untuk membuat tabel Produk
    def create_produk_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE Produk (
                    Kode_Produk CHAR(4) NOT NULL PRIMARY KEY,
                    Nama_Produk VARCHAR(25),
                    Jenis_Produk VARCHAR(20),
                    Harga INT(30)
                )
            """)
            print("Tabel 'Produk' berhasil dibuat.")
        except mysql.connector.Error as e:
            print(f"Terjadi kesalahan saat membuat tabel Produk: {e}")

    # Fungsi untuk membuat tabel Struk
    def create_struk_table(self):
        try:
            self.cur.execute("""
                CREATE TABLE Struk (
                    No_Transaksi CHAR(4) NOT NULL PRIMARY KEY,
                    Nama_Pegawai VARCHAR(15),
                    Nama_Produk VARCHAR(25),
                    Jumlah_Produk INT(30),
                    Total_Harga INT(30)
                )
            """)
            print("Tabel 'Struk' berhasil dibuat.")
        except mysql.connector.Error as e:
            print(f"Terjadi kesalahan saat membuat tabel Struk: {e}")

    # Fungsi untuk menambahkan foreign key ke tabel Struk
    def add_foreign_keys(self):
        try:
            self.cur.execute("""
                ALTER TABLE Struk
                    ADD FOREIGN KEY (Nama_Pegawai)
                    REFERENCES Pegawai(Nama_Pegawai)
            """)
            self.cur.execute("""
                ALTER TABLE Struk
                    ADD FOREIGN KEY (Nama_Produk)
                    REFERENCES Produk(Nama_Produk)
            """)
            self.cur.execute("""
                ALTER TABLE Struk
                    ADD FOREIGN KEY (No_Transaksi)
                    REFERENCES Transaksi(No_Transaksi)
            """)
            print("Foreign keys berhasil ditambahkan.")
        except mysql.connector.Error as e:
            print(f"Terjadi kesalahan saat menambahkan foreign keys: {e}")

    def tambah_pegawai(self, nik, nama_pegawai, alamat):
        try:
            if not nik or not nama_pegawai or not alamat:
                print("Semua inputan harus diisi. Gagal menambahkan Pegawai.")
                return
            
            self.cur.execute("SELECT COUNT(*) FROM Pegawai WHERE NIK = %s", (nik,))
            result = self.cur.fetchone()

            if result[0] > 0:
                print(f"NIK {nik} sudah terdaftar. Gagal menambahkan Pegawai.")
            else:
                query = "INSERT INTO Pegawai (NIK, Nama_Pegawai, Alamat) VALUES (%s, %s, %s)"
                self.cur.execute(query, (nik, nama_pegawai, alamat))
                self.conn.commit()
                print("Data Pegawai berhasil ditambahkan.")
        except Error as e:
            print(f"Terjadi kesalahan saat menambahkan pegawai: {e}")

    def lihat_pegawai(self):
        try:
            self.cur.execute("SELECT * FROM Pegawai")
            return self.cur.fetchall()
        except Error as e:
            print(f"Terjadi kesalahan saat membaca data pegawai: {e}")

    def update_pegawai(self, nik, nama_pegawai=None, alamat=None):
        try:
            query = "UPDATE Pegawai SET"
            updates = []
            values = []

            if nama_pegawai:
                updates.append("Nama_Pegawai = %s")
                values.append(nama_pegawai)

            if alamat:
                updates.append("Alamat = %s")
                values.append(alamat)

            if updates:
                query += " " + ", ".join(updates) + " WHERE NIK = %s"
                values.append(nik)
                self.cur.execute(query, tuple(values))
                self.conn.commit()
                print("Data Pegawai berhasil diperbarui.")
            else:
                print("Tidak ada data yang diperbarui.")
        except Error as e:
            print(f"Terjadi kesalahan saat memperbarui pegawai: {e}")

    def hapus_pegawai(self, nik):
        try:
            self.cur.execute("DELETE FROM Pegawai WHERE NIK = %s", (nik,))
            self.conn.commit()
            print("Data Pegawai berhasil dihapus.")
        except Error as e:
            print(f"Terjadi kesalahan saat menghapus pegawai: {e}")

    def tambah_produk(self, nama_produk, jenis_produk, harga):
        try:
            self.cur.execute("SELECT COUNT(*) FROM Produk")
            result = self.cur.fetchone()
            product_count = result[0] + 1  
            kode_produk = f"P{product_count:02d}" 

            query = "INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga) VALUES (%s, %s, %s, %s)"
            self.cur.execute(query, (kode_produk, nama_produk, jenis_produk, harga))
            self.conn.commit()
            print(f"Data Produk dengan Kode {kode_produk} berhasil ditambahkan.")
        except Error as e:
            print(f"Terjadi kesalahan saat menambahkan produk: {e}")

    def lihat_produk(self):
        try:
            self.cur.execute("SELECT * FROM Produk")
            return self.cur.fetchall()
        except Error as e:
            print(f"Terjadi kesalahan saat membaca data produk: {e}")

    def update_produk(self, kode_produk, nama_produk=None, jenis_produk=None, harga=None):
        try:
            query = "UPDATE Produk SET"
            updates = []
            values = []

            if nama_produk:
                updates.append("Nama_Produk = %s")
                values.append(nama_produk)

            if jenis_produk:
                updates.append("Jenis_Produk = %s")
                values.append(jenis_produk)

            if harga is not None:
                updates.append("Harga = %s")
                values.append(harga)

            if updates:
                query += " " + ", ".join(updates) + " WHERE Kode_Produk = %s"
                values.append(kode_produk)
                self.cur.execute(query, tuple(values))
                self.conn.commit()
                print("Data Produk berhasil diperbarui.")
            else:
                print("Tidak ada data yang diperbarui.")
        except Error as e:
            print(f"Terjadi kesalahan saat memperbarui produk: {e}")

    def hapus_produk(self, kode_produk):
        try:
            self.cur.execute("DELETE FROM Produk WHERE Kode_Produk = %s", (kode_produk,))
            self.conn.commit()
            print("Data Produk berhasil dihapus.")
        except Error as e:
            print(f"Terjadi kesalahan saat menghapus produk: {e}")

    def tambah_transaksi(self):
        try:
            # Membuat No Transaksi otomatis (contoh: T01, T02, ...)
            self.cur.execute("SELECT COUNT(*) FROM Transaksi")
            result = self.cur.fetchone()
            transaksi_count = result[0] + 1  # Menghitung transaksi berikutnya
            no_transaksi = f"T{transaksi_count:02d}"  # Format No Transaksi

            # Menentukan detail transaksi (tanggal dan waktu saat ini)
            tanggal_transaksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            detail_transaksi = tanggal_transaksi  # Menggunakan tanggal dan waktu saat transaksi

            # Input dari pengguna
            nama_pegawai = input("Masukkan nama pegawai: ").strip()
            if not nama_pegawai:
                print("Nama pegawai tidak boleh kosong.")
                return

            # Menambahkan produk ke dalam transaksi
            produk_list = []
            while True:
                nama_produk = input("Masukkan nama produk: ").strip()
                if not nama_produk:
                    print("Nama produk tidak boleh kosong.")
                    return

                jumlah_produk_input = input("Masukkan jumlah produk: ").strip()
                if not jumlah_produk_input.isdigit() or int(jumlah_produk_input) <= 0:
                    print("Jumlah produk harus berupa angka positif.")
                    return
                jumlah_produk = int(jumlah_produk_input)

                # Cek apakah produk tersedia dalam tabel Produk
                self.cur.execute("SELECT Harga FROM Produk WHERE Nama_Produk = %s", (nama_produk,))
                result_produk = self.cur.fetchone()

                if result_produk:
                    harga_produk = result_produk[0]
                    total_harga = harga_produk * jumlah_produk
                    produk_list.append((nama_produk, jumlah_produk, total_harga))
                else:
                    print(f"Produk '{nama_produk}' tidak ditemukan dalam database.")
                
                # Tanya apakah ingin menambah produk lagi
                tambah_lagi = input("Apakah ingin menambah produk lagi? (ya/tidak): ").strip().lower()
                if tambah_lagi != 'ya':
                    break

            # Cek apakah pegawai tersedia dalam tabel Pegawai
            self.cur.execute("SELECT * FROM Pegawai WHERE Nama_Pegawai = %s", (nama_pegawai,))
            result_pegawai = self.cur.fetchone()

            if result_pegawai:
                # Menambahkan data ke tabel Transaksi
                query_transaksi = "INSERT INTO Transaksi (No_Transaksi, Detail_Transaksi) VALUES (%s, %s)"
                self.cur.execute(query_transaksi, (no_transaksi, detail_transaksi))
                self.conn.commit()

                # Menambahkan data ke tabel Struk untuk setiap produk yang dibeli
                for produk in produk_list:
                    nama_produk, jumlah_produk, total_harga = produk
                    # Pastikan bahwa setiap produk dimasukkan dengan entri unik ke tabel Struk
                    query_struk = """INSERT INTO Struk (No_Transaksi, Nama_Pegawai, Nama_Produk, Jumlah_Produk, Total_Harga) 
                                    VALUES (%s, %s, %s, %s, %s)"""
                    self.cur.execute(query_struk, (no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga))
                    self.conn.commit()

                print(f"Transaksi dan struk dengan No Transaksi {no_transaksi} berhasil ditambahkan.")
            else:
                print(f"Pegawai '{nama_pegawai}' tidak ditemukan dalam database.")
        except Error as e:
            print(f"Terjadi kesalahan saat menambahkan transaksi: {e}")

    def cetak_struk(self):
        try:
            # Menampilkan struk yang baru saja ditambahkan (struk terakhir berdasarkan No Transaksi)
            self.cur.execute("""
                SELECT s.No_Transaksi, s.Nama_Pegawai, s.Nama_Produk, s.Jumlah_Produk, s.Total_Harga
                FROM Struk s
                WHERE s.No_Transaksi = (SELECT MAX(No_Transaksi) FROM Struk)
            """)
            
            rows = self.cur.fetchall()

            if rows:
                total_harga = 0
                print("=" * 30)
                print("           STRUK TRANSAKSI")
                print("=" * 30)
                
                for row in rows:
                    no_transaksi = row[0]
                    nama_pegawai = row[1]
                    nama_produk = row[2]
                    jumlah_produk = row[3]
                    total_harga_produk = row[4]
                    
                    total_harga += total_harga_produk  # Menambahkan harga total per produk ke total harga keseluruhan

                    # Mencetak detail produk per transaksi
                    print(f"Nama Produk     : {nama_produk}")
                    print(f"Jumlah Produk   : {jumlah_produk}")
                    print(f"Total Per Item  : Rp {total_harga_produk:,.0f}")
                    print("-" * 30)

                # Menampilkan total harga
                print(f"Total Harga     : Rp {total_harga:,.0f}")
                print("=" * 30)
            else:
                print("Tidak ada data struk.")
        except Error as e:
            print(f"Terjadi kesalahan saat membaca data struk: {e}")


    def close_connection(self):
        try:
            self.cur.close()
            self.conn.close()
        except Error as e:
            print(f"Terjadi kesalahan saat menutup koneksi: {e}")

if __name__ == "__main__":
    crud = penjualan()

    while True:
        print("\nMenu Warung Penjualan Sederhana:")
        print("1. Pegawai")
        print("2. Produk")
        print("3. Transaksi")
        print("4. Struk")
        print("5. Exit")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            while True:
                print("\nMenu Pegawai:")
                print("1. Tambah Pegawai")
                print("2. Lihat Pegawai")
                print("3. Update Pegawai")
                print("4. Hapus Pegawai")
                print("5. Kembali ke Menu Utama")
                
                pilihan = input("Pilih menu pegawai: ")

                if pilihan == "1":
                    nik = input("Masukkan NIK: ")
                    nama = input("Masukkan Nama Pegawai: ")
                    alamat = input("Masukkan Alamat: ")
                    crud.tambah_pegawai(nik, nama, alamat)
                elif pilihan == "2":
                    pegawai = crud.lihat_pegawai()
                    print(tabulate(pegawai, headers=["NIK", "Nama_Pegawai", "Alamat"], tablefmt="grid"))
                elif pilihan == "3":
                    nik = input("Masukkan NIK yang akan diupdate: ")
                    nama = input("Masukkan Nama baru (kosongkan jika tidak ingin diubah): ")
                    alamat = input("Masukkan Alamat baru (kosongkan jika tidak ingin diubah): ")
                    crud.update_pegawai(nik, nama if nama else None, alamat if alamat else None)
                elif pilihan == "4":
                    nik = input("Masukkan NIK yang akan dihapus: ")
                    crud.hapus_pegawai(nik)
                elif pilihan == "5":
                    break
                else:
                    print("Pilihan tidak valid(Pilih Menu Yang Sesuai).")

        elif pilih == "2":
            while True:
                print("\nMenu Produk:")
                print("1. Tambah Produk")
                print("2. Lihat Produk")
                print("3. Update Produk")
                print("4. Hapus Produk")
                print("5. Kembali ke Menu Utama")
                
                pilihan = input("Pilih menu produk: ")

                if pilihan == "1":
                    nama = input("Masukkan Nama Produk: ")
                    jenis = input("Masukkan Jenis Produk: ")
                    harga = float(input("Masukkan Harga Produk: "))
                    crud.tambah_produk(nama, jenis, harga)
                elif pilihan == "2":
                    produk = crud.lihat_produk()
                    print(tabulate(produk, headers=["Kode_Produk", "Nama_Produk", "Jenis_Produk", "Harga"], tablefmt="grid"))
                elif pilihan == "3":
                    kode_produk = input("Masukkan Kode Produk yang akan diupdate: ")
                    nama = input("Masukkan Nama baru (kosongkan jika tidak ingin diubah): ")
                    jenis = input("Masukkan Jenis baru (kosongkan jika tidak ingin diubah): ")
                    harga = input("Masukkan Harga baru (kosongkan jika tidak ingin diubah): ")
                    crud.update_produk(kode_produk, nama if nama else None, jenis if jenis else None, float(harga) if harga else None)
                elif pilihan == "4":
                    kode_produk = input("Masukkan Kode Produk yang akan dihapus: ")
                    crud.hapus_produk(kode_produk)
                elif pilihan == "5":
                    break
                else:
                    print("Pilihan tidak valid (Masukkan Menu Yang Sesuai).")

        elif pilih == "3":
            while True:
                print("\nMenu Transaksi:")
                print("1. Tambah Transaksi")
                print("2. Kembali ke Menu Utama")
                
                pilihan = input("Pilih menu transaksi: ")

                if pilihan == "1":
                    crud.tambah_transaksi()
                elif pilihan == "2":
                    break
                else:
                    print("Pilihan tidak valid (Masukkan Menu Yang Sesuai).")

        elif pilih == "4":
            while True:
                print("\nMenu Struk:")
                print("1. Lihat Struk Terbaru")
                print("2. Kembali ke Menu Utama")
                
                pilihan = input("Pilih menu struk: ")

                if pilihan == "1":
                    crud.cetak_struk()
                elif pilihan == "2":
                    break
                else:
                    print("Pilihan tidak valid (Masukkan Menu Yang Sesuai).")

        elif pilih == "5":
            crud.close_connection()
            break
        else:
            print("Pilihan tidak valid (Masukkan Menu Yang Sesuai).")