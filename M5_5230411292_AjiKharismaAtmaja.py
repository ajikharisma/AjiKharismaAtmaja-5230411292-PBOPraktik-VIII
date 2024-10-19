from tabulate import tabulate
# buat class (judul,penyanyi,genre)
class Musik:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

# buat 3 class turunan dari class music method(display,add,delete)
class MusikPop(Musik):

    def display_all(lagu_list):
        headers = ["Judul","Penyanyi","Genre"]
        table = [[lagu.judul, lagu.penyanyi, lagu.genre]for lagu in lagu_list]
        print(tabulate(table, headers, tablefmt="grid"))
    
    def add(self):
        print(f"Lagu {self.judul} telah ditambahkan ke playlist")
    
    def delete(self):
        print(f"Lagu {self.judul} telah dihapus dari playlist")

class MusikJawa(Musik):
    def display_all(lagu_list):
        headers = ["Judul","Penyanyi","Genre"]
        table = [[lagu.judul, lagu.penyanyi, lagu.genre]for lagu in lagu_list]
        print(tabulate(table, headers, tablefmt="grid"))

    def add(self):
        print(f"Lagu {self.judul} telah ditambahkan ke playlist")

    def delete(self):
        print(f"Lagu {self.judul} telah dihapus dari playlist")

class MusikRock(Musik):
    def display_all(lagu_list):
        headers = ["Judul","Penyanyi","Genre"]
        table = [[lagu.judul, lagu.penyanyi, lagu.genre]for lagu in lagu_list]
        print(tabulate(table, headers, tablefmt="grid"))

    def add(self):
        print(f"Lagu {self.judul} telah ditambahkan ke playlist")

    def delete(self):
        print(f"Lagu {self.judul} telah dihapus dari playlist")

def displayAllSorted(lagu_list):
    headers = ["Judul","Penyanyi","Genre"]
    sorted_lagu_list = sorted(lagu_list,key=lambda lagu: lagu.judul)
    table = [[lagu.judul, lagu.penyanyi, lagu.genre]for lagu in sorted_lagu_list]
    print(tabulate(table, headers, tablefmt="grid"))

def cariPenyanyi(lagu_list,nama_penyanyi):
    headers = ['judul','penyanyi','genre']
    result = [lagu for lagu in lagu_list if nama_penyanyi.lower()in lagu.penyanyi.lower()]
    if result:
        table = [[lagu.judul, lagu.penyanyi, lagu.genre]for lagu in result]
        print(tabulate(table, headers, tablefmt="grid"))
    else:
        print("Lagu tidak ditemukan")




musik_pop = [
    MusikPop("Ingkar","Tulus","POP"),
    MusikPop("Pesan Terakhir","Lyodra","POP"),
    MusikPop("Hadapi Berdua","Tiara Andini","POP"),
    MusikPop("Gala Bunga Matahari","Sal Priadi","POP"),
    MusikPop("Terlalu Cinta","Yovie Widianto dan Lyodra","POP")
]
musik_jawa = [
    MusikJawa("Anak Lanang","Ndarboy Genk","Musik jawa"),
    MusikJawa("Rungkad","Happy Asmara","Musik jawa"),
    MusikJawa("Kalah"," Aftershine","Musik jawa"),
    MusikJawa("Dadi Siji","Woro Widowati","Musik jawa"),
    MusikJawa("Sanes","GuyonWaton X Denny Caknan","Musik jawa")
]
musik_rock = [
    MusikRock("Kangen","Dewa 19","Rock"),
    MusikRock("Terlalu Manis","Slank","Rock"),
    MusikRock("Jangan pernah berubah","ST12","Rock"),
    MusikRock("Janji","Gigi","Rock"),
    MusikRock("Pelangi di matamu","Jamrud","Rock")
]

allLagu = musik_pop + musik_jawa + musik_rock
while True:
    print("\nMenu Playlist Musik:")
    print("1. Musik Pop")
    print("2. Musik Jawa")
    print("3. Musik Rock")
    print("4. Display ALL")
    print("5. Cari Musik")
    print("6. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        print("\n Musik Pop:")
        print("1.Display Song")
        print("2.Add Song")
        print("3.Delete Song")
        print("4.Kembali")
        pilihan2 = input("masukkan sub menu musik pop: ")
        if pilihan2 == "1":
            MusikPop.display_all(musik_pop)
        elif pilihan2 == "2":
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan penyanyi: ")
            musik_pop.append(MusikPop(judul, penyanyi, "Pop"))
            print(f"Lagu {judul} telah ditambahkan ke playlist")
        elif pilihan2 == "3":
            judul = input("Masukkan judul lagu yang ingin dihapus: ")
            for i in range(len(musik_pop)):
                if musik_pop[i].judul == judul:
                    del musik_pop[i]
                    print(f"Lagu {judul} telah dihapus dari playlist")
                    break
        elif pilihan2 == "4":
            continue
        else:
            print("Pilihan tidak tersedia")
    if pilihan == "2":
        print("\n Musik Jawa:")
        print("1.Display Song")
        print("2.Add Song")
        print("3.Delete Song")
        print("4.Kembali")
        pilihan2 = input("masukkan sub menu musik jawa: ")
        if pilihan2 == "1":
            MusikJawa.display_all(musik_jawa)
        elif pilihan2 == "2":
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan penyanyi: ")
            musik_jawa.append(MusikJawa(judul, penyanyi, "musik jawa"))
            print(f"Lagu {judul} telah ditambahkan ke playlist")
        elif pilihan2 == "3":
            judul = input("Masukkan judul lagu yang ingin dihapus: ")
            for i in range(len(musik_jawa)):
                if musik_jawa[i].judul == judul:
                    del musik_jawa[i]
                    print(f"Lagu {judul} telah dihapus dari playlist")
                    break
        elif pilihan2 == "4":
            continue
        else:
            print("Pilihan tidak tersedia")
    elif pilihan == "3":
        print("\n Musik Rock:")
        print("1.Display Song")
        print("2.Add Song")
        print("3.Delete Song")
        print("4.Kembali")
        pilihan2 = input("masukkan sub menu musik rock: ")
        if pilihan2 == "1":
            MusikRock.display_all(musik_rock)
        elif pilihan2 == "2":
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan penyanyi: ")
            musik_rock.append(MusikRock(judul, penyanyi, "Rock"))
            print(f"Lagu {judul} telah ditambahkan ke playlist")
        elif pilihan2 == "3":
            judul = input("Masukkan judul lagu yang ingin dihapus: ")
            for i in range(len(musik_rock)):
                if musik_rock[i].judul == judul:
                    del musik_rock[i]
                    print(f"Lagu {judul} telah dihapus dari playlist")
                    break
        elif pilihan2 == "4":
            continue
        else:
            print("Pilihan tidak tersedia")

    # Tampilin semua lagu dari 3 genre berdasarkan abjad A-z
    elif pilihan == "4":
        displayAllSorted(allLagu)
    elif pilihan == "5":
        # cari  musik berdasarkan penyanyi
        penyanyi = input("Masukkan penyanyi: ")
        cariPenyanyi(allLagu, penyanyi)

        



