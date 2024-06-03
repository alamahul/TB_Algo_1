class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    
    def tambah_di_depan(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def tambah_di_tengah(self, index, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    print("Index di luar jangkauan")
                    return
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    def tambah_di_belakang(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def hapus_di_depan(self):
        if self.head is None:
            print("List kosong")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def hapus_di_tengah(self, index):
        if self.head is None:
            print("List kosong")
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                print("Index di luar jangkauan")
                return
            current = current.next
        if current.next is None:
            print("Index di luar jangkauan")
            return
        if current.next.next:
            current.next.next.prev = current
        current.next = current.next.next

    def hapus_di_belakang(self):
        if self.head is None:
            print("List kosong")
            return
        current = self.head
        while current.next:
            current = current.next
        if current.prev:
            current.prev.next = None
        else:
            self.head = None

    def cetak_list(self):
        if self.head is None:
            print("List kosong")
            return 0
        current = self.head
        while current:
            # if current.data == '0' or current.data == 0:
            #     current = current.next
            # else:
            print(f'[{current.data}]', end=" ")
            current = current.next
        return 1
    
    def cetak_list_awal(self):
        if self.head is None:
            print("List kosong")
            return 0
        current = self.head
        print(current.data)
        return current.data

    def cetak_list_tengah(self, index):
        if self.head is None:
            print("List kosong")
            return 0
        current = self.head
        for _ in range(index - 1):
            if current is None:
                print("Index di luar jangkauan")
                return 0
            current = current.next
        if current.next is None:
            print("Index di luar jangkauan")
            return 0
        if current.next.next:
            print(current.next.data)
            return current.next.data

    def cetak_list_belakang(self):
        if self.head is None:
            print("List kosong")
            return 0
        current = self.head
        while current.next:
            current = current.next
        if current.prev:
            print(current.data)
            return current.data

    def cari_list(self, cari):
        if self.head is None:
            print("list kosong")
            return 0
        else:
            current = self.head
            i = 0
            while current is not None:
                 if current.data == cari:
                     return i
                 i = i + 1
                 current = current.next
            return None   
# Contoh penggunaan
if __name__ == "__main__":
    linked_list = DoublyLinkedList()

    linked_list.tambah_di_belakang(0)
    linked_list.tambah_di_belakang(20)
    linked_list.tambah_di_belakang(30)
    linked_list.tambah_di_depan(5)
    linked_list.tambah_di_tengah(1, 15)
    linked_list.tambah_di_tengah(0, 7)

    # print("Linked list setelah penambahan:")
    # linked_list.cetak_list_awal()
    
    print(linked_list.cari_list(30))
    linked_list.cetak_list()
    # linked_list.cetak_list_tengah(2)
    # linked_list.cetak_list_belakang()

    linked_list.hapus_di_depan()
    linked_list.hapus_di_depan()
    # linked_list.hapus_di_tengah(4)
    # linked_list.hapus_di_belakang()

    # print("\nLinked list setelah penghapusan:")
    linked_list.cetak_list()
