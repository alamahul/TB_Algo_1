import random
class Node:
    def __init__(self, Kategori, NamaProduk=None, HargaProduk=None, KategoriProduk=None, pelanggan=None):
        self.Kategori = Kategori
        self.NamaProduk = NamaProduk
        self.HargaProduk = HargaProduk
        self.KategoriProduk = KategoriProduk
        self.next = None
        self.prev = None
        self.pelanggan = pelanggan
        self.quantity = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def tambah_kategori(self, nama_kategori):
        new_kategori = Node(nama_kategori, None, None, None, None)
        if self.head == None:
            self.head = new_kategori
        else:
            new_kategori.next = self.head
            self.head.prev = new_kategori
            self.head = new_kategori

    def tambah_awal_list(self, NamaProduk, HargaProduk, KategoriProduk):
        new_Produk = Node(None, NamaProduk, HargaProduk, KategoriProduk, None)
        if self.head == None:
            self.head = new_Produk
        else:
            new_Produk.next = self.head
            self.head.prev = new_Produk
            self.head = new_Produk

    def tambah_tengah_list_berdasarkan_kategori(self, Kategori, NamaProduk, HargaProduk, KategoriProduk): # Hanya bisa untuk Kategori tengah dan akhir
        new_Produk = Node(None, NamaProduk, HargaProduk, KategoriProduk, None)
        if self.head == None:
            self.head = new_Produk
        else:
            current = self.head
            while current.next:
                if current.Kategori == Kategori:
                    new_Produk.next = current.next
                    new_Produk.prev = current
                    if current.next:
                        current.next.prev = new_Produk
                    current.next = new_Produk
                    return   
                current = current.next
    

    def tambah_akhir_list(self, NamaProduk, HargaProduk, KategoriProduk):
        new_Produk = Node(None, NamaProduk, HargaProduk, KategoriProduk)
        if self.head == None:
            self.head = new_Produk
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_Produk
            current.prev = current

    def hapus_awal_list(self):
        if self.head is None:
            print("List kosong")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def hapus_tengah_list_berdasarkan_nama_Produk(self, nama_Produk):
        if self.head is None:
            print("List kosong, tidak ada yang dihapus")
            return

        current = self.head
        while current:
            if current.NamaProduk == nama_Produk:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next

    def hapus_akhir_list(self):
        if self.head is None:
            print("List kosong, tidak ada yang dihapus")
            return

        current = self.head
        if current.next is None:
            self.head = None
            return

        while current.next.next:
            current = current.next

        current.next = None

    def cetak_list(self):
        if self.head == None:
            print('List masih kosong')
            return
        current = self.head
        while current:
            if current.Kategori != None:
                print(f'\nKategori : {current.Kategori}')
            if current.NamaProduk != None and current.HargaProduk != None and current.KategoriProduk != None:
                print(f'{current.NamaProduk} <=> {current.HargaProduk} <=> {current.KategoriProduk}')
            current = current.next
        return

    def hitung_Produk_berdasarkan_kategori(self, kategori):
        if self.head == None:
            print('List masih kosong')
            return
        current = self.head
        JumlahProduk = 1
        while current.next:
            if current.KategoriProduk == kategori:
                JumlahProduk += 1
            current = current.next
        return JumlahProduk

    def hitung_semua_Produk(self):
        if self.head == None:
            return 'List masih kosong'
        current = self.head
        JumlahProduk = 1
        while current.next:
            if current.Kategori is None:
                JumlahProduk += 1
            current = current.next
        return JumlahProduk

    def hapus_semua_Produk_berdasarkan_kategori(self, kategori):
        if self.head == None:
            print('linklist kosong')
            return
        if kategori == 'Kosmetik':
            JumlahProduk = self.hitung_Produk_berdasarkan_kategori(kategori)
            for _ in range((JumlahProduk - 1)):
                self.hapus_awal_list()
        elif kategori == 'Minuman':
            JumlahProduk = self.hitung_Produk_berdasarkan_kategori(kategori)
            for _ in range(JumlahProduk):
                self.hapus_akhir_list()
        elif kategori == 'BahanBaku':
            JumlahProduk = self.hitung_Produk_berdasarkan_kategori(kategori)
            current = self.head
            while current:
                if current.KategoriProduk == kategori:
                    for _ in range(JumlahProduk):
                        self.hapus_tengah_list_berdasarkan_nama_Produk(current.NamaProduk)
                current = current.next 

    def hapus_semua_Produk(self):
        if self.head == None:
            print('linklist kosong')
            return
        current = self.head
        while current:
            if current.NamaProduk != None and current.HargaProduk != None:
                self.hapus_tengah_list_berdasarkan_nama_Produk(current.NamaProduk)
            current = current.next
        current = self.head
        while current:
            if current.Kategori == None:
                self.hapus_akhir_list()
            current = current.next
        
        print('Semua Produk berhasil dihapus')

    def updateProduk_berdasarkan_nama(self, NamaProduk, HargaProduk):
        if self.head == None:
            print('Produk tidak tersedia')
            return
        current = self.head
        while current:
            if current.NamaProduk == NamaProduk:
                current.HargaProduk = int(HargaProduk)
            current = current.next
        return
    
    def validasiproduk(self, NamaProduk=None):
        if self.head == None:
            print('Produk Belum tersedia')
            return True
        current = self.head
        while current:
            if current.NamaProduk == NamaProduk:
                print('Produk Sudah tersedia')
                return False
            current = current.next
        print('Produk Belum tersedia')
        return True
    
    def JumlahSemuaProduk(self):
        JumlahBarang = 0
        if self.head == None:
            return JumlahBarang
        current = self.head
        while current:
            if current.Kategori == None:
                JumlahBarang += 1
            current = current.next
        return JumlahBarang
        
    def cetak_produk(self):
        if self.head == None:
            return
        if self.head.NamaProduk == None:
            return
        current = self.head
        print('| \t\tKategori Kosmetik\t\t\t\t ')
        while current:
            if current.KategoriProduk == 'Kosmetik':
                print(f'| Nama Produk : {current.NamaProduk}, Harga Produk : {current.HargaProduk} ')
            current = current.next

        current = self.head
        print('| \t\tKategori Bahan Baku\t\t\t\t ')
        while current:
            if current.KategoriProduk == 'BahanBaku':
                print(f'| Nama Produk : {current.NamaProduk}, Harga Produk : {current.HargaProduk} ')
            current = current.next
        
        current = self.head
        print('| \t\tKategori Minuman\t\t\t\t ')
        while current:
            if current.KategoriProduk == 'Minuman':
                print(f'| Nama Produk : {current.NamaProduk}, Harga Produk : {current.HargaProduk} ')
            current = current.next
        return
    def pesanan(self, nama, jumlah):
        if self.head == None:
            print('Produk tidak tersedia')
            return
        current = self.head
        while current:
            if current.NamaProduk == nama:
                current.pelanggan = current
                current.pelanggan.quantity = jumlah
            current = current.next
        
        return
    
    def hapusPesanan(self, nama):
        if self.head == None:
            print('Produk tidak tersedia')
            return
        current = self.head
        while current:
            if current.NamaProduk == nama:
                current.pelanggan = None
            current = current.next
        return
        # pilihan = int(input("Masukan Pilihan anda : "))
        # if pilihan == 1:
        #     valid = True
        #     while valid == True:
        #         NamaProduk = input('Masukan nama barang = ')
        #         JumlahBarang = input('Masukan nama barang = ')
    def hapusSeluruhPesanan(self):
        if self.head == None:
            print('Produk sudah tidak tersedia')
            return
        current = self.head
        while current:
            current.pelanggan = None
            current = current.next
        print('Semua Produk Pelanggan telah terhapus')
        return
            
    def keranjang(self):
        if self.head == None:
            print('Produk sudah tidak tersedia')
            return
        current = self.head
        while current:
            if current.pelanggan != None:
                print(f'Nama Produk : {current.pelanggan.NamaProduk}, Jumlah Produk : {current.pelanggan.quantity}')
            current = current.next            

    def cetak_tagihan(self):
        if self.head == None:
            print('Produk tidak tersedia')
            return
        current = self.head
        nama = input('Nama Pelanggan : ')
        NoHp = input('No. Hp Pelanggan : ')
        NoTagihan = random.randint(100, 1000)

        totalHargaKosmetik = 0
        totalHargaBahanBaku = 0
        totalHargaMinuman = 0
        print('| ------------------------------------------------------------------------------ |')
        print('| \t\t\t\tSelamat Datang\t\t\t\t ')
        print('| ------------------------------------------------------------------------------ |')
        print(f'| Nama Pelanggan : {nama} ')
        print(f'| No Hp : {NoHp}')
        print(f'| No Tagihan : {NoTagihan}')
        print('| ------------------------------------------------------------------------------ |')
        print('| \t\t\t\tKategori Kosmetik\t\t\t\t ')
        print('| ------------------------------------------------------------------------------ |')
        while current:
            if current.KategoriProduk == 'Kosmetik':
                if current.pelanggan != None:
                    print(f'| Nama Produk : {current.pelanggan.NamaProduk}, Quantity : {current.pelanggan.quantity},Harga Produk : {current.HargaProduk} ')
                    totalHargaKosmetik += int(current.pelanggan.quantity)*current.HargaProduk
            current = current.next
        current = self.head
        print('| ------------------------------------------------------------------------------ |')
        print('| \t\t\t\tKategori Bahan Baku\t\t\t\t')
        print('| ------------------------------------------------------------------------------ |')
        while current:
            if current.KategoriProduk == 'BahanBaku':
                if current.pelanggan != None:
                    print(f'| Nama Produk : {current.pelanggan.NamaProduk}, Quantity : {current.pelanggan.quantity},Harga Produk : {current.HargaProduk} ')
                    totalHargaBahanBaku += int(current.pelanggan.quantity)*current.HargaProduk
            current = current.next
        current = self.head
        print('| ------------------------------------------------------------------------------ |')
        print('| \t\t\t\tKategori Minuman\t\t\t\t')
        print('| ------------------------------------------------------------------------------ |')
        while current:
            if current.KategoriProduk == 'Minuman':
                if current.pelanggan != None:
                    print(f'| Nama Produk : {current.pelanggan.NamaProduk}, Quantity : {current.pelanggan.quantity},Harga Produk : {current.HargaProduk} ')
                    totalHargaMinuman += int(current.pelanggan.quantity)*current.HargaProduk
            current = current.next
        print('| ------------------------------------------------------------------------------ |')
        print('| \t\t\t\t   Total\t\t\t\t')
        print('| ------------------------------------------------------------------------------ |')
        print('| Total Harga Kosmetik = ', totalHargaKosmetik)   
        print('| Total Harga Bahan Baku = ', totalHargaBahanBaku)   
        print('| Total Harga Minuman = ', totalHargaMinuman)
        print('| Total dari Seluruh Kategori = Rp. ', totalHargaKosmetik + totalHargaBahanBaku + totalHargaMinuman)
        print('| ============================================================================== |')
        print()

    def detailPesanan(self, namaProduk, detailProduk):
        if self.head == None:
            print('List kosong')
            return
        current = self.head
        while current:
            if current.pelanggan != None:
                if current.pelanggan.NamaProduk == namaProduk:
                    if detailProduk == 'Harga':
                        return current.pelanggan.HargaProduk
                    if detailProduk == 'Jumlah':
                        return current.pelanggan.quantity
                    if detailProduk == 'Kategori':
                        return current.pelanggan.KategoriProduk
            current = current.next
        print('Detail Produk tidak ditemukan')
        return
    
    def cekPesanan(self, nama):
        if self.head == None:
            print('List kosong')
            return False
        current = self.head
        while current:
            if current.pelanggan != None:
                if current.pelanggan.NamaProduk == nama:
                    return True
            current = current.next
        return False
    

# DLL = DoublyLinkedList()
# DLL.tambah_kategori('Minuman')
# DLL.tambah_kategori('BahanBaku')
# DLL.tambah_kategori('Kosmetik')

# DLL.tambah_awal_list('Sampo', 5000, 'Kosmetik')
# DLL.tambah_awal_list('Skincare', 7500, 'Kosmetik')

# DLL.tambah_tengah_list_berdasarkan_kategori('BahanBaku', 'Bumbu', 4000, 'BahanBaku')
# DLL.tambah_tengah_list_berdasarkan_kategori('BahanBaku', 'Beras', 14000, 'BahanBaku')

# DLL.tambah_akhir_list('Cola-Cola', 8000, 'Minuman')
# DLL.tambah_akhir_list('Power F', 1000, 'Minuman')

# DLL.pesanan('Sampo', 4)
# DLL.pesanan('Bumbu', 2)
# DLL.pesanan('Cola-Cola', 3)

# print(DLL.cekPesanan('Power F'))

# print(DLL.detailPesanan('Sampo', 'Harga'))

# DLL.cetak_list()
# # print()


# # print('Hapus Awal list')
# # DLL.hapus_awal_list() # Skincare terhapus
# # DLL.cetak_list()

# # print('Hapus akhir list')
# # DLL.hapus_akhir_list() # Power F terhapus
# # DLL.cetak_list()

# # print('Hapus tengah list')
# # DLL.hapus_tengah_list_berdasarkan_nama_produk('Masako') # Masako terhapus


# # print('Hitung semua Produk berdasarkan kategori')
# # print(DLL.hitung_Produk_berdasarkan_kategori('Minuman')) # JumlahProduk di kategori

# # print('Hitung Semua Produk')
# # print(DLL.hitung_semua_Produk())

# # print('Hapus Produk berdasarkan kategori')
# # DLL.hapus_semua_Produk_berdasarkan_kategori('BahanBaku')
# # DLL.cetak_list()



# while True:
#     print()
#     print("============ Program Manajemen Retail ==========")
#     print("1. Tambah Produk")
#     print("2. Update Produk")
#     print("3. Hapus Produk dari Nama Produk")
#     print("4. Hapus Semua Produk dari kategori")
#     print("5. Hapus Semua Produk")
#     print("6. Layani Pelanggan")
#     print('7. Exit')
#     print()
#     print('Data List')
#     DLL.cetak_list()
#     print()
#     pilihan = int(input('Masukan pilihan anda : '))

#     if pilihan == 1:
#         print('Masukan Datanya')
#         valid = False
#         while valid == False:
#             NamaProdukBaru = input('Nama Produk : ')
#             valid = DLL.validasiproduk(NamaProdukBaru)
#         HargaProdukBaru = int(input('Harga Produk : '))
#         KategoriProdukBaru = input('Kategori Produk : ')
#         if KategoriProdukBaru == 'Kosmetik':
#             DLL.tambah_awal_list(NamaProdukBaru, HargaProdukBaru, KategoriProdukBaru)
#             print('Produk berhasil ditambah')
#         elif KategoriProdukBaru == 'Minuman':
#             DLL.tambah_akhir_list(NamaProdukBaru, HargaProdukBaru, KategoriProdukBaru)
#             print('Produk berhasil ditambah')
#         elif KategoriProdukBaru == 'BahanBaku':
#             DLL.tambah_tengah_list_berdasarkan_kategori(KategoriProdukBaru, NamaProdukBaru, HargaProdukBaru, KategoriProdukBaru)
#             print('Produk berhasil ditambah')
#         else:
#             print('inputan tidak valid')

#     elif  pilihan == 2:
#         if DLL.JumlahSemuaProduk() == 0:
#             print('Produk belum tersedia')
#         else:
#             print('Masukan Datanya')
#             valid = True
#             while valid == True:
#                 NamaProduk = input('Nama Produk : ')
#                 valid = DLL.validasiproduk(NamaProduk)
#             HargaProdukBaru = int(input('Harga Produk : '))
#             DLL.updateProduk_berdasarkan_nama(NamaProduk, HargaProdukBaru)
#             print('Produk berhasil diupdate')   

#     elif pilihan == 3:
#         NamaProduk = input('Nama Produk yang akan dihapus : ')
#         DLL.hapus_tengah_list_berdasarkan_nama_Produk(NamaProduk)
#         print('Produk berhasil dihapus')
#     elif pilihan == 4:
#         kategori = input('Masukan Kategori : ')
#         DLL.hapus_semua_Produk_berdasarkan_kategori(kategori)
#         print('Produk berhasil dihapus')
#     elif pilihan == 5:
#         DLL.hapus_semua_Produk()
#     elif pilihan == 6:
#         kondisi = True
#         while kondisi:
#             print('Daftar Produk')
#             DLL.cetak_produk()
#             print()
#             print('1. Tambahkan Pesanan')
#             print('2. Update Pesanan')
#             print('3. Hapus Pesanan')
#             print('4. Hapus Semua Pesanan')
#             print('5. Cetak Tagihan')
#             print('6. Kelola Barang')
#             print()
#             print('Keranjang Pelanggan')
#             DLL.keranjang()
#             print()
#             pilihan = int(input('Masukan pilihan Anda :'))
            
#             if pilihan == 1:
#                 nama = input('Nama Produk :')
#                 jumlah = input('Jumlah Produk :')
#                 DLL.pesanan(nama, jumlah)
#             elif pilihan == 2:
#                 nama = input('Nama Produk :')
#                 jumlah = input('Jumlah Produk :')
#                 DLL.pesanan(nama, jumlah)
#             elif pilihan == 3:
#                 nama = input('Nama Produk :')
#                 DLL.hapusPesanan(nama)
#                 print('Produk berhasil')
#             elif pilihan == 4:
#                 DLL.hapusSeluruhPesanan()
#             elif pilihan == 5:
#                 DLL.cetak_tagihan()
#             elif pilihan == 6:
#                 kondisi = False
#             else:
#                 print('Pilihan tidak valid')
        


#     elif pilihan == 7:
#         input('tekan enter untuk keluar')
#         break
#     else:
#         pass





        