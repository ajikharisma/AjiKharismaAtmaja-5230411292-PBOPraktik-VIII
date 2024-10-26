from tabulate import tabulate
class order:
    order_count = 0
    def __init__(self,nama=str,details=str):
        order.order_count += 1
        self.ID = order.order_count
        self.nama = nama
        self.details = details
    
    # tambah order
    def set_order(self):
        self._id =id
        self.nama = nama
        self.details = details

    def lihatOrder(set_order):
        headers = ("Id","Nama","Details")
        table = [[order.ID,order.nama,order.details]for order in set_order ]
        print(tabulate(table, headers, tablefmt="fancy_grid"))

    
class delivery:
    delivery_count = 0
    def __init__(self,order,date=str,alamat=str):
        delivery.delivery_count += 1
        self.ID = delivery.delivery_count
        self.order = order
        self.date = date
        self.alamat = alamat
    
    def display(self):
        headers = ("Delivery ID", "Order ID", "Nama", "Details", "Tanggal", "Alamat")
        table = [[self.ID, self.order.ID, self.order.nama, self.order.details, self.date, self.alamat]]
        print(tabulate(table, headers, tablefmt="fancy_grid"))

setOrder = []
setDelivery = []
while True:
    print("Menu Rumah Makan")
    print("1. Order Makanan")
    print("2. Lihat order")
    print("3. Proses pengiriman")
    print("4.Lihat pengiriman")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        nama = input("Masukkan nama orderan: ")
        details = input("Masukkan details orderan: ")
        orderan = order(nama,details)
        setOrder.append(orderan)
        print("Orderan berhasil")

    elif pilihan == "2":
        if setOrder:
            order.lihatOrder(setOrder)
        else:
            print("Belum ada order yang tersedia.")
    elif pilihan == "3":
        if not setOrder:
            print("Tidak ada order yang tersedia untuk pengiriman.")
        else:
            print("=== Daftar Order Tersedia ===")
            order.lihatOrder(setOrder)
            order_id = int(input("Masukkan ID Order untuk Pengiriman: "))

            order_dipilih = None
            for order in setOrder:
                if order.ID == order_id:
                    order_dipilih = order
                    break
            
            if order_dipilih is None:
                print("Order dengan ID tersebut tidak ditemukan.")
            else:
                tanggal = input("Masukkan Tanggal Pengiriman (YYYY-MM-DD): ")
                alamat = input("Masukkan Alamat Pengiriman: ")
                delivery = delivery(order_dipilih, tanggal, alamat)
                setDelivery.append(delivery)
                print("Pengiriman telah diproses.")
    elif pilihan == "4":
        if setDelivery:
            for delivery in setDelivery:
                delivery.display()
        else:
            print("Belum ada pengiriman yang diproses.")
    elif pilihan == "5":
        print("Terima Kasih Telah Menggunakan Sistem ini")
        break
    else:
        print("Pilihan tidak tersedia")