import tkinter as tk
from collections import deque
from tkinter import ttk,messagebox

queue_a = deque() #LOKET A
queue_b = deque() #LOKET B

class antrian:
    def __init__(self,root):
        self.root = root
        self.root.title("Sistem Antrian Sembako")
        self.root.geometry("800x800")
        self.root.configure(bg="teal")
        self.widget_create()
    
    def widget_create(self):
        # TITLE TABEL
        self.label = tk.Label(self.root, text="Antrian Sembako Kabupaten Sleman",font=("Arial",25,"bold"),background="teal",foreground="white")
        self.label.pack(pady=10)


        # INPUT JUMLAH PAKET SEMBAKO DI LOKET A
        self.porsi_label_a = tk.Label(self.root, text="Jumlah Paket Sembako di Loket A:",background="teal",foreground="white",font=("Arial",10,"bold"))
        self.porsi_label_a.pack(pady=5)
        self.porsi_entry_a = tk.Entry(self.root, width=10)
        self.porsi_entry_a.pack(pady=5)

        # INPUT JUMLAH PAKET SEMBAKO DI LOKET B
        self.porsi_label_b = tk.Label(self.root, text="Jumlah Paket Sembako di Loket B:",background="teal",foreground="white",font=("Arial",10,"bold"))
        self.porsi_label_b.pack(pady=5)
        self.porsi_entry_b = tk.Entry(self.root, width=10)
        self.porsi_entry_b.pack(pady=5)

        # INPUT NAMA 
        self.nama_label = tk.Label(self.root, text="Nama Warga :",background="teal",foreground="white",font=("Arial",10,"bold"))
        self.nama_label.pack(pady=5)
        self.nama_entry = tk.Entry(self.root, width=15)
        self.nama_entry.pack(pady=5)

        #  TOMBOL TAMBAH ANTRIAN
        frame_tambah = tk.Frame(self.root,background="teal")
        frame_tambah.pack(pady=5)

        #TOMBOL TAMBAH KE LOKET A
        self.tambah_a_button = tk.Button(frame_tambah, text="Tambah Ke Antrian Loket A",activebackground="red",background="white",command=self.tambah_antrian_a)
        self.tambah_a_button.pack(side=tk.LEFT, padx=10)
        #TOMBOL TAMBAH KE LOKET B
        self.tambah_b_button = tk.Button(frame_tambah, text="Tambah Ke Antrian Loket B",activebackground="red",background="white",command=self.tambah_antrian_b)
        self.tambah_b_button.pack(side=tk.RIGHT, padx=10)

        # FRAME UNTUK TABEL ANTRIAN DAN TOMBOL PANGGIL
        frame_tabel = tk.Frame(self.root)
        frame_tabel.pack(pady=20)


        # LABEL PEMANGGILAN
        self.pemanggilan_label = tk.Label(self.root, text="Memanggil: ", font=("Arial", 15, "bold"),background="teal",foreground="white")
        self.pemanggilan_label.pack(pady=20)

        # TABEL DAFTAR ANTRIAN LOKET A
        frame_a = tk.Frame(frame_tabel)
        frame_a.pack(side=tk.LEFT, padx=20)

        self.label_a = tk.Label(frame_a, text="Daftar Antrian di Loket A")
        self.label_a.pack(pady=5)
        self.pesanan_label_a = ttk.Treeview(frame_a, columns=("No Antrian", "Nama"), show="headings",height=8)
        self.pesanan_label_a.heading("No Antrian", text="No Antrian")
        self.pesanan_label_a.heading("Nama", text="Nama")
        self.pesanan_label_a.column("No Antrian", width=100, anchor="center")
        self.pesanan_label_a.column("Nama", width=150, anchor="center")
        self.pesanan_label_a.pack(pady=5)

        #TOMBOL PANGGIL LOKET A
        self.panggil_a_button = tk.Button(frame_a, text="Panggil Antrian Loket A",activebackground="red",background="yellow", command=self.panggil_berikutnya_a)
        self.panggil_a_button.pack(pady=5)

        # TABEL DAFTAR ANTRIAN LOKET B
        frame_b = tk.Frame(frame_tabel)
        frame_b.pack(side=tk.RIGHT, padx=20)

        self.label_b = tk.Label(frame_b, text="Daftar Antrian Di Loket B")
        self.label_b.pack(pady=5)
        self.pesanan_label_b = ttk.Treeview(frame_b, columns=("No Antrian", "Nama"), show="headings",height=8)
        self.pesanan_label_b.heading("No Antrian", text="No Antrian")
        self.pesanan_label_b.heading("Nama", text="Nama")
        self.pesanan_label_b.column("No Antrian", width=100, anchor="center")
        self.pesanan_label_b.column("Nama", width=150, anchor="center")
        self.pesanan_label_b.pack(pady=5)

        #TOMBOL PANGGIL LOKET B
        self.panggil_b_button = tk.Button(frame_b, text="Panggil Antrian Loket B",activebackground="red",background="yellow", command=self.panggil_berikutnya_b)
        self.panggil_b_button.pack(pady=5)
    
    # TAMBAH ANTRIAN A
    def tambah_antrian_a(self):
        nama = self.nama_entry.get()
        if nama in queue_a or nama in queue_b:
            messagebox.showerror("Error", f"Nama {nama} sudah ada dalam antrian di salah satu loket.")
            return
        self.tambah_antrian(queue_a, self.porsi_entry_a, self.pesanan_label_a)

    # TAMBAH ANTRIAN B
    def tambah_antrian_b(self):
        nama = self.nama_entry.get()
        if nama in queue_a or nama in queue_b:
            messagebox.showerror("Error", f"Nama {nama} sudah ada dalam antrian di salah satu loket.")
            return
        self.tambah_antrian(queue_b, self.porsi_entry_b, self.pesanan_label_b)

    def tambah_antrian(self, queue, porsi_entry, pesanan_label):
        nama = self.nama_entry.get()
        porsi = porsi_entry.get()
        if nama != "" and porsi != "":
            try:
                porsi = int(porsi)
                if len(queue) < porsi:
                    queue.append(nama)
                    pesanan_label.insert("", "end", values=(str(len(queue)), nama))
                    self.nama_entry.delete(0, tk.END)
                else:
                    messagebox.showinfo("Info", "Antrian penuh")
            except ValueError:
                messagebox.showerror("Error", "Porsi harus angka.")
        else:
            messagebox.showerror("Error", "Nama dan jumlah paket sembako harus diisi.")

    
    #PANGGIL ANTRIAN A
    def panggil_berikutnya_a(self):
        if queue_a:
            # Panggil antrean pertama
            self.pemanggilan_label.config(text="Memanggil Untuk Mengambil Sembako Di Loket A : " + queue_a.popleft())
            self.update_tabel_a()
        else:
            messagebox.showinfo("Info", "Antrian sudah kosong")
        
    #PANGGIL ANTRIAN B
    def panggil_berikutnya_b(self):
        if queue_b:
            # Panggil antrean pertama
            self.pemanggilan_label.config(text="Memanggil Untuk Mengambil Sembako Di Loket B : " + queue_b.popleft())
            self.update_tabel_b()
        else:
            messagebox.showinfo("Info", "Antrian sudah kosong")
    
    
    def update_tabel_a(self):
        # Hapus semua data di tabel
        for item in self.pesanan_label_a.get_children():
            self.pesanan_label_a.delete(item)
        # Masukkan data antrean yang tersisa
        for idx, nama in enumerate(queue_a, start=1):
            self.pesanan_label_a.insert("", "end", values=(str(idx), nama))

    def update_tabel_b(self):
        # Hapus semua data di tabel
        for item in self.pesanan_label_b.get_children():
            self.pesanan_label_b.delete(item)
        # Masukkan data antrean yang tersisa
        for idx, nama in enumerate(queue_b, start=1):
            self.pesanan_label_b.insert("", "end", values=(str(idx), nama))

if __name__  ==  '__main__':
    root = tk.Tk()
    app = antrian(root)
    root.mainloop()