class Node:
    def __init__(self, id, nama_barang, harga):
        self.id = id
        self.nama_barang = nama_barang
        self.harga = harga
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_node_diawal(self, id, nama_barang, harga):
        new_node = Node(id, nama_barang, harga)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def tambah_node_ditengah(self, posisi, id, nama_barang, harga):
        if not self.head:
            print("List kosong")
            return
        current = self.head
        while current:
            if current.id == posisi:
                new_node = Node(id, nama_barang, harga)
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                return
            current = current.next
        print("ID tidak ditemukan")

    def tambah_node_diakhir(self, id, nama_barang, harga):
        new_node = Node(id, nama_barang, harga)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def hapus_node_diawal(self):
        if not self.head:
            print("List kosong")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def hapus_node_ditengah(self, posisi):
        if not self.head:
            print("List kosong")
            return
        current = self.head
        while current:
            if current.id == posisi:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
        print("ID tidak ditemukan")

    def hapus_node_diakhir(self):
        if not self.head:
            print("List kosong")
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def hapus_nama_dan_harga(self, id):
        if not self.head:
            print("List kosong")
            return
        current = self.head
        while current:
            if current.id == id:
                current.nama_barang = None
                current.harga = None
                return
            current = current.next
        print("ID tidak ditemukan")

    def tambah_nama_dan_harga(self, id, nama_barang, harga):
        if not self.head:
            print("List kosong")
            return
        current = self.head
        while current:
            if current.id == id:
                current.nama_barang = nama_barang
                current.harga = harga
                return
            current = current.next
        print("ID tidak ditemukan")

    def tambah_id_saja(self, id):
        new_node = Node(id, None, None)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def sorting(self):
        if not self.head:
            print("List kosong")
            return
        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if current.nama_barang > next_node.nama_barang:
                    # current.id, next_node.id = next_node.id, current.id
                    current.nama_barang, next_node.nama_barang = next_node.nama_barang, current.nama_barang
                    current.harga, next_node.harga = next_node.harga, current.harga
                next_node = next_node.next
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(f"{current.id} <=> {current.nama_barang} <=> {current.harga}")
            current = current.next

# Contoh penggunaan
dll = DoublyLinkedList()
dll.tambah_node_diakhir(1, "Sampo", 5000)
dll.tambah_node_diakhir(2, "Autan", 3000)
dll.tambah_node_diakhir(3, "Odol", 7000)

print("Sebelum sorting:")
dll.display()

print("\nSetelah sorting:")
dll.sorting()
dll.display()

print("\nSetelah hapus nama dan harga tanpa menghapus ID (1):")
dll.hapus_nama_dan_harga(1)
dll.display()

print("\nSetelah tambah ID saja (4):")
dll.tambah_id_saja(4)
dll.display()
