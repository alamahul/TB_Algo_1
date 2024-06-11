from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk

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

    def tambah_tengah_list_berdasarkan_kategori(self, Kategori, NamaProduk, HargaProduk, KategoriProduk):
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
            messagebox.showinfo("Info", "List kosong")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def hapus_tengah_list_berdasarkan_nama_Produk(self, nama_Produk):
        if self.head is None:
            messagebox.showinfo("Info", "List kosong, tidak ada yang dihapus")
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
            messagebox.showinfo("Info", "List kosong, tidak ada yang dihapus")
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
            return 'List masih kosong'
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
            return 'List masih kosong'
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
            return 'linklist kosong'
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
            return 'linklist kosong'
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

        return 'Semua Produk berhasil dihapus'

    def updateProduk_berdasarkan_nama(self, NamaProduk, HargaProduk):
        if self.head == None:
            return 'Produk tidak tersedia'
        current = self.head
        while current:
            if current.NamaProduk == NamaProduk:
                current.HargaProduk = int(HargaProduk)
            current = current.next
        return 'Produk berhasil diupdate'

    def validasiproduk(self, NamaProduk=None):
        if self.head == None:
            return 'Produk Belum tersedia'
        current = self.head
        while current:
            if current.NamaProduk == NamaProduk:
                return 'Produk Sudah tersedia'
            current = current.next
        return 'Produk Belum tersedia'

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
            return 'Produk tidak tersedia'
        current = self.head
        while current:
            if current.NamaProduk == nama:
                current.pelanggan = current
                current.pelanggan.quantity = jumlah
            current = current.next

        return

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Retail Management Program")
        self.geometry("800x600")

        self.inventory = DoublyLinkedList()

        # Create GUI elements
        self.label_title = Label(self, text="Retail Management System", font=("Arial", 24))
        self.label_title.pack(pady=10)

        self.frame_add_product = Frame(self, bd=1, relief=SUNKEN)
        self.frame_add_product.pack(pady=20)

        self.label_add_product = Label(self.frame_add_product, text="Add Product:")
        self.label_add_product.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.label_nama_produk = Label(self.frame_add_product, text="Nama Produk:")
        self.label_nama_produk.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_nama_produk = Entry(self.frame_add_product, width=30)
        self.entry_nama_produk.grid(row=1, column=1, padx=10, pady=5)

        self.label_harga_produk = Label(self.frame_add_product, text="Harga Produk:")
        self.label_harga_produk.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_harga_produk = Entry(self.frame_add_product, width=30)
        self.entry_harga_produk.grid(row=2, column=1, padx=10, pady=5)

        self.label_kategori_produk = Label(self.frame_add_product, text="Kategori Produk:")
        self.label_kategori_produk.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_kategori_produk = Entry(self.frame_add_product, width=30)
        self.entry_kategori_produk.grid(row=3, column=1, padx=10, pady=5)

        self.button_tambah_produk = Button(self.frame_add_product, text="Tambah Produk", command=self.tambah_produk)
        self.button_tambah_produk.grid(row=4, column=1, padx=10, pady=10)

        self.frame_remove_product = Frame(self, bd=1, relief=SUNKEN)
        self.frame_remove_product.pack(pady=20)

        self.label_remove_product = Label(self.frame_remove_product, text="Remove Product:")
        self.label_remove_product.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.label_nama_produk_hapus = Label(self.frame_remove_product, text="Nama Produk:")
        self.label_nama_produk_hapus.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_nama_produk_hapus = Entry(self.frame_remove_product, width=30)
        self.entry_nama_produk_hapus.grid(row=1, column=1, padx=10, pady=5)

        self.button_hapus_produk = Button(self.frame_remove_product, text="Hapus Produk", command=self.hapus_produk)
        self.button_hapus_produk.grid(row=2, column=1, padx=10, pady=10)

        self.frame_display_inventory = Frame(self, bd=1, relief=SUNKEN)
        self.frame_display_inventory.pack(pady=20)

        self.label_display_inventory = Label(self.frame_display_inventory, text="Display Inventory:")
        self.label_display_inventory.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.button_cetak_inventory = Button(self.frame_display_inventory, text="Cetak Inventory", command=self.cetak_inventory)
        self.button_cetak_inventory.grid(row=1, column=0, padx=10, pady=10)

        self.button_cetak_produk = Button(self.frame_display_inventory, text="Cetak Produk", command=self.cetak_produk)
        self.button_cetak_produk.grid(row=1, column=1, padx=10, pady=10)

        self.frame_update_product = Frame(self, bd=1, relief=SUNKEN)
        self.frame_update_product.pack(pady=20)

        self.label_update_product = Label(self.frame_update_product, text="Update Product:")
        self.label_update_product.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.label_nama_produk_update = Label(self.frame_update_product, text="Nama Produk:")
        self.label_nama_produk_update.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_nama_produk_update = Entry(self.frame_update_product, width=30)
        self.entry_nama_produk_update.grid(row=1, column=1, padx=10, pady=5)

        self.label_harga_produk_update = Label(self.frame_update_product, text="Harga Produk Baru:")
        self.label_harga_produk_update.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_harga_produk_update = Entry(self.frame_update_product, width=30)
        self.entry_harga_produk_update.grid(row=2, column=1, padx=10, pady=5)

        self.button_update_produk = Button(self.frame_update_product, text="Update Produk", command=self.update_produk)
        self.button_update_produk.grid(row=3, column=1, padx=10, pady=10)

        self.frame_pesanan = Frame(self, bd=1, relief=SUNKEN)
        self.frame_pesanan.pack(pady=20)

        self.label_pesanan = Label(self.frame_pesanan, text="Pesanan:")
        self.label_pesanan.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.label_nama_pesanan = Label(self.frame_pesanan, text="Nama Produk:")
        self.label_nama_pesanan.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_nama_pesanan = Entry(self.frame_pesanan, width=30)
        self.entry_nama_pesanan.grid(row=1, column=1, padx=10, pady=5)

        self.label_jumlah_pesanan = Label(self.frame_pesanan, text="Jumlah Produk:")
        self.label_jumlah_pesanan.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_jumlah_pesanan = Entry(self.frame_pesanan, width=30)
        self.entry_jumlah_pesanan.grid(row=2, column=1, padx=10, pady=5)

        self.button_tambah_pesanan = Button(self.frame_pesanan, text="Tambah Pesanan", command=self.tambah_pesanan)
        self.button_tambah_pesanan.grid(row=3, column=1, padx=10, pady=10)

        self.button_exit = Button(self, text="Exit", command=self.destroy)
        self.button_exit.pack(pady=20)

    def tambah_produk(self):
        nama_produk = self.entry_nama_produk.get()
        harga_produk = self.entry_harga_produk.get()
        kategori_produk = self.entry_kategori_produk.get()

        if nama_produk == "" or harga_produk == "" or kategori_produk == "":
            messagebox.showwarning("Input Error", "Mohon lengkapi semua kolom!")
            return

        self.inventory.tambah_awal_list(nama_produk, harga_produk, kategori_produk)
        messagebox.showinfo("Success", "Produk berhasil ditambahkan ke inventory!")

        # Clear input fields after adding
        self.entry_nama_produk.delete(0, END)
        self.entry_harga_produk.delete(0, END)
        self.entry_kategori_produk.delete(0, END)

    def hapus_produk(self):
        nama_produk = self.entry_nama_produk_hapus.get()

        if nama_produk == "":
            messagebox.showwarning("Input Error", "Mohon masukkan nama produk yang ingin dihapus!")
            return

        self.inventory.hapus_tengah_list_berdasarkan_nama_Produk(nama_produk)
        messagebox.showinfo("Success", "Produk berhasil dihapus dari inventory!")

        # Clear input field after deleting
        self.entry_nama_produk_hapus.delete(0, END)

    def cetak_inventory(self):
        inventory_content = self.inventory.cetak_list()
        if inventory_content == 'List masih kosong':
            messagebox.showinfo("Info", "Inventory masih kosong")
        else:
            messagebox.showinfo("Inventory Content", inventory_content)

    def cetak_produk(self):
        self.inventory.cetak_produk()

    def update_produk(self):
        nama_produk = self.entry_nama_produk_update.get()
        harga_produk_baru = self.entry_harga_produk_update.get()

        if nama_produk == "" or harga_produk_baru == "":
            messagebox.showwarning("Input Error", "Mohon lengkapi semua kolom!")
            return

        result = self.inventory.updateProduk_berdasarkan_nama(nama_produk, harga_produk_baru)
        messagebox.showinfo("Update Result", result)

        # Clear input fields after updating
        self.entry_nama_produk_update.delete(0, END)
        self.entry_harga_produk_update.delete(0, END)

    def tambah_pesanan(self):
        nama_produk = self.entry_nama_pesanan.get()
        jumlah_produk = self.entry_jumlah_pesanan.get()

        if nama_produk == "" or jumlah_produk == "":
            messagebox.showwarning("Input Error", "Mohon lengkapi semua kolom!")
            return

        result = self.inventory.tambah_pesanan(nama_produk, jumlah_produk)
        if result == "Produk tidak ditemukan":
            messagebox.showerror("Error", "Produk tidak ditemukan dalam inventory!")
        else:
            messagebox.showinfo("Success", "Pesanan berhasil ditambahkan!")

        # Clear input fields after adding order
        self.entry_nama_pesanan.delete(0, END)
        self.entry_jumlah_pesanan.delete(0, END)

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = GUI()
    app.run()