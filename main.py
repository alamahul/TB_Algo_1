import const as const
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

import DoublyLinkedList as DBL



ProdukList = DBL.DoublyLinkedList()

# Penambahan Kategori
ProdukList.tambah_kategori('Minuman')
ProdukList.tambah_kategori('BahanBaku')
ProdukList.tambah_kategori('Kosmetik')
# End

# ProdukList.cetak_list()

if not os.path.exists(f'{const.PATHPARENTFILE}/Tagihan'):
    os.mkdir(f'{const.PATHPARENTFILE}/Tagihan')
#functionality part
def send_email():
    def send_email():
        try:
            ob=smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            reciever_address = recieverEntry.get()
            ob.sendmail(senderEntry.get(), reciever_address, message)
            ob.quit()
            messagebox.showinfo('Sukses', 'Tagihan telah berhasi dikirim', parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error', 'Ada yang Error, Coba beberapa saat lagi', parent=root1)



    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Tagihan kosong')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('send email')
        root1.config(bg=const.primary)
        root1.resizable(0,0)

        senderFrame = LabelFrame(root1, text='Pengiriman', font=('Arial', 16, 'bold'), bd=6, bg=const.primary, fg=const.light)
        senderFrame.grid(row=0,column=0, padx=40, pady=20)

        senderIDLabel = Label(senderFrame, text="Pengirim Email", font=('Arial', 14 , 'bold'), bg=const.primary, fg=const.light)
        senderIDLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry = Entry(senderFrame, font=('Arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('Arial', 14 , 'bold'), bg=const.primary, fg=const.light)
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('Arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show="*")
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        # ----------------------------------

        recipeintFrame = LabelFrame(root1, text='Penerima', font=('Arial', 16, 'bold'), bd=6, bg=const.primary, fg=const.light)
        recipeintFrame.grid(row=1,column=0, padx=40, pady=20)

        recieverLabel = Label(recipeintFrame, text="Penerima Email", font=('Arial', 14 , 'bold'), bg=const.primary, fg=const.light)
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipeintFrame, font=('Arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipeintFrame, text="Pesan", font=('Arial', 14 , 'bold'), bg=const.primary, fg=const.light)
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(recipeintFrame, font=('Arial', 14, 'bold'), bd=2, relief=SUNKEN, height=14, width=67)
        email_textarea.grid(row=2, column=0 , columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END))


        sendButton = Button(root1, text="Kirim", font=('Arial', 14, 'bold'), width=15, command=send_email)
        sendButton.grid(row=2, column=0, pady=20)

        root.mainloop()

def clear():
    # Hapus Semua List Produk
    # Kategori Kosmetik
    ProdukList.hapusPesanan('Sabun Mandi')
    ProdukList.hapusPesanan('Sabun Wajah')
    ProdukList.hapusPesanan('Parfum')
    ProdukList.hapusPesanan('Sampo')
    ProdukList.hapusPesanan('Skincare')
    ProdukList.hapusPesanan('Autan')
    # Kategori Kosmetik
    ProdukList.hapusPesanan('Nasi')
    ProdukList.hapusPesanan('Minyak')
    ProdukList.hapusPesanan('Bumbu')
    ProdukList.hapusPesanan('Gandum')
    ProdukList.hapusPesanan('Gula')
    ProdukList.hapusPesanan('Teh')
    # Kategori Minuman
    ProdukList.hapusPesanan('Fanta')
    ProdukList.hapusPesanan('Power F')
    ProdukList.hapusPesanan('Sprite')
    ProdukList.hapusPesanan('Pepsi')
    ProdukList.hapusPesanan('Coca Cola')
    ProdukList.hapusPesanan('Kratindeng')
    # End
    bathsoapEntry.delete(0,END)
    facescreamEntry.delete(0,END)
    hairsprayEntry.delete(0,END)
    bodylotionEntry.delete(0,END)
    fashwashEntry.delete(0,END)
    hairgelEntry.delete(0,END)

    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    gandumEntry.delete(0,END)
    bumbuEntry.delete(0,END)
    gulaEntry.delete(0,END)
    tehEntry.delete(0,END)

    fantaEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    powerfEntry.delete(0,END)
    spriteEntry.delete(0,END)
    cocacolaEntry.delete(0,END)
    kratindengEntry.delete(0,END)

    cosmenticpriceEntry.delete(0,END)
    grocerpriceEntry.delete(0,END)
    drinkpriceEntry.delete(0,END)

    cosmentictaxEntry.delete(0,END)
    grocertaxEntry.delete(0,END)
    drinktaxEntry.delete(0,END)
    
    # Penambahan angka nol
    bathsoapEntry.insert(END, 0)
    facescreamEntry.insert(END, 0)
    hairsprayEntry.insert(END, 0)
    bodylotionEntry.insert(END, 0)
    fashwashEntry.insert(END, 0)
    hairgelEntry.insert(END, 0)

    riceEntry.insert(END, 0)
    oilEntry.insert(END, 0)
    gandumEntry.insert(END, 0)
    bumbuEntry.insert(END, 0)
    gulaEntry.insert(END, 0)
    tehEntry.insert(END, 0)

    fantaEntry.insert(END, 0)
    pepsiEntry.insert(END, 0)
    powerfEntry.insert(END, 0)
    spriteEntry.insert(END, 0)
    cocacolaEntry.insert(END, 0)
    kratindengEntry.insert(END, 0)

    cosmenticpriceEntry.insert(END, 0)
    grocerpriceEntry.insert(END, 0)
    drinkpriceEntry.insert(END, 0)

    cosmentictaxEntry.insert(END, 0)
    grocertaxEntry.insert(END, 0)
    drinktaxEntry.insert(END, 0)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    textarea.delete(1.0, END)


    
    pass

def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Tagihan kosong')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')

def save_bill():
    global billnumber
    result = messagebox.askyesno('Konfirmasi', 'Apakah kamu ingin menyimpan tagihanya?')
    if result:
        bill_contents = textarea.get(1.0, END)
        file = open(f'{const.PATHPARENTFILE}/Tagihan/{billnumber}.txt', 'w')
        file.write(bill_contents)
        file.close()
        messagebox.showinfo('Berhasil', f'{billnumber}.txt Berhasil disimpan')
        billnumber=random.randint(100, 1000)

billnumber=random.randint(100, 1000)

def search_bill():
    for i in os.listdir(f'{const.PATHPARENTFILE}/Tagihan/'):
        if i.split('.')[0]==billnumberEntry.get():
            f = open(f'{const.PATHPARENTFILE}/Tagihan/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    
        else:
            messagebox.showerror('Error', 'Nomor Tagihan tidak Valid')


def set_text(entry, text):
    entry.delete(0,END)
    entry.insert(0,text)
    return




def total():
    global totalcosmeticprice,totalgroceryprice,totalcolddrinkprice
    global totalcosmetictax, totalgrocerytax, totalcolddrinktax
    
    # Tambah diawal/Akhir
    
    # cosmeticslist.display()
    # Hapus ditengah

    # cosmetic price calculation
    # Penambahan variable harga
    HargaKosmetik1 = 0
    HargaKosmetik2 = 0
    HargaKosmetik3 = 0
    HargaKosmetik4 = 0
    HargaKosmetik5 = 0
    HargaKosmetik6 = 0
    
    # Masukan/Pengahapusan ke Produk List  
    if int(bathsoapEntry.get()) != 0:
        if ProdukList.validasiproduk('Sabun Mandi') == True : ProdukList.tambah_awal_list('Sabun Mandi', 3000, 'Kosmetik')
        ProdukList.pesanan('Sabun Mandi', int(bathsoapEntry.get()))
        HargaKosmetik1 += ProdukList.detailPesanan('Sabun Mandi', 'Harga')*ProdukList.detailPesanan('Sabun Mandi', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Sabun Mandi') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Sabun Mandi')
        HargaKosmetik1 = 0
    if int(facescreamEntry.get()) != 0:
        if ProdukList.validasiproduk('Sabun Wajah') == True : ProdukList.tambah_awal_list('Sabun Wajah', 10000, 'Kosmetik')
        ProdukList.pesanan('Sabun Wajah', int(facescreamEntry.get()))
        HargaKosmetik2 += ProdukList.detailPesanan('Sabun Wajah', 'Harga')*ProdukList.detailPesanan('Sabun Wajah', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Sabun Wajah') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Sabun Wajah')
        HargaKosmetik2 = 0
    if int(fashwashEntry.get()) != 0:
        if ProdukList.validasiproduk('Parfum') == True : ProdukList.tambah_awal_list('Parfum', 7000, 'Kosmetik')
        ProdukList.pesanan('Parfum', int(fashwashEntry.get()))
        HargaKosmetik3 += ProdukList.detailPesanan('Parfum', 'Harga')*ProdukList.detailPesanan('Parfum', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Parfum') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Parfum')
        HargaKosmetik3 = 0
    if int(hairsprayEntry.get()) != 0:
        if ProdukList.validasiproduk('Sampo') == True : ProdukList.tambah_awal_list('Sampo', 5000, 'Kosmetik')
        ProdukList.pesanan('Sampo', int(hairsprayEntry.get()))
        HargaKosmetik4 += ProdukList.detailPesanan('Sampo', 'Harga')*ProdukList.detailPesanan('Sampo', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Sampo') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Sampo')
        HargaKosmetik4 = 0
    if int(hairgelEntry.get()) != 0:
        if ProdukList.validasiproduk('Skincare') == True : ProdukList.tambah_awal_list('Skincare', 15000, 'Kosmetik')
        ProdukList.pesanan('Skincare', int(hairgelEntry.get()))
        HargaKosmetik5 += ProdukList.detailPesanan('Skincare', 'Harga')*ProdukList.detailPesanan('Skincare', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Skincare') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Skincare')
        HargaKosmetik5 = 0
    if int(bodylotionEntry.get()) != 0:
        if ProdukList.validasiproduk('Autan') == True : ProdukList.tambah_awal_list('Autan', 1000, 'Kosmetik')
        ProdukList.pesanan('Autan', int(bodylotionEntry.get()))
        HargaKosmetik6 += ProdukList.detailPesanan('Autan', 'Harga')*ProdukList.detailPesanan('Autan', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Autan') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Autan')
        HargaKosmetik6 = 0
    


    # print('List Pesanan')
    # ProdukList.keranjang()
    
    # soapprice=int(bathsoapEntry.get())*3000
    # facescreamprice=int(facescreamEntry.get())*10000
    # fashwashprice=int(fashwashEntry.get())*7000
    # hairsprayprice=int(hairsprayEntry.get())*5000
    # hairgelprice=int(hairgelEntry.get())*15000
    # bodylotionprice=int(bodylotionEntry.get())*1000
     
    

    totalcosmeticprice=HargaKosmetik1+HargaKosmetik2+HargaKosmetik3+HargaKosmetik4+HargaKosmetik5+HargaKosmetik6
    totalcosmetictax = totalcosmeticprice * 0.25
    set_text(cosmentictaxEntry, f'Rp. {totalcosmetictax}')
    set_text(cosmenticpriceEntry, f'Rp. {totalcosmeticprice}')


    # # grocery price calcutaion
    # Penambahan variable harga
    HargaBahanBaku1 = 0
    HargaBahanBaku2 = 0
    HargaBahanBaku3 = 0
    HargaBahanBaku4 = 0
    HargaBahanBaku5 = 0
    HargaBahanBaku6 = 0
    
    # Masukan/Pengahapusan ke Produk List  
    if int(riceEntry.get()) != 0:
        if ProdukList.validasiproduk('Nasi') == True : ProdukList.tambah_tengah_list_berdasarkan_kategori('BahanBaku','Nasi', 25000, 'BahanBaku')
        ProdukList.pesanan('Nasi', int(riceEntry.get()))
        HargaBahanBaku1 += ProdukList.detailPesanan('Nasi', 'Harga')*ProdukList.detailPesanan('Nasi', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Nasi') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Nasi')
        HargaBahanBaku1 = 0
    if int(oilEntry.get()) != 0:
        if ProdukList.validasiproduk('Minyak') == True : ProdukList.tambah_tengah_list_berdasarkan_kategori('BahanBaku','Minyak', 30000, 'BahanBaku')
        ProdukList.pesanan('Minyak', int(oilEntry.get()))
        HargaBahanBaku2 += ProdukList.detailPesanan('Minyak', 'Harga')*ProdukList.detailPesanan('Minyak', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Minyak') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Minyak')
        HargaBahanBaku2 = 0
    if int(bumbuEntry.get()) != 0:
        if ProdukList.validasiproduk('Bumbu') == True : ProdukList.tambah_tengah_list_berdasarkan_kategori('BahanBaku','Bumbu', 5000, 'BahanBaku')
        ProdukList.pesanan('Bumbu', int(bumbuEntry.get()))
        HargaBahanBaku3 += ProdukList.detailPesanan('Bumbu', 'Harga')*ProdukList.detailPesanan('Bumbu', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Bumbu') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Bumbu')
        HargaBahanBaku3 = 0
    if int(gandumEntry.get()) != 0:
        if ProdukList.validasiproduk('Gandum') == True : ProdukList.tambah_tengah_list_berdasarkan_kategori('BahanBaku','Gandum', 20000, 'BahanBaku')
        ProdukList.pesanan('Gandum', int(gandumEntry.get()))
        HargaBahanBaku4 += ProdukList.detailPesanan('Gandum', 'Harga')*ProdukList.detailPesanan('Gandum', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Gandum') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Gandum')
        HargaBahanBaku4 = 0
    if int(gulaEntry.get()) != 0:
        if ProdukList.validasiproduk('Gula') == True : ProdukList.tambah_tengah_list_berdasarkan_kategori('BahanBaku','Gula', 10000, 'BahanBaku')
        ProdukList.pesanan('Gula', int(gulaEntry.get()))
        HargaBahanBaku5 += ProdukList.detailPesanan('Gula', 'Harga')*ProdukList.detailPesanan('Gula', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Gula') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Gula')
        HargaBahanBaku5 = 0
    if int(tehEntry.get()) != 0:
        if ProdukList.validasiproduk('Teh') == True : ProdukList.tambah_tengah_list_berdasarkan_kategori('BahanBaku','Teh', 3000, 'BahanBaku')
        ProdukList.pesanan('Teh', int(tehEntry.get()))
        HargaBahanBaku6 += ProdukList.detailPesanan('Teh', 'Harga')*ProdukList.detailPesanan('Teh', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Teh') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Teh')
        HargaBahanBaku6 = 0

    # riceprice = int(riceEntry.get())*25000
    # oilprice = int(oilEntry.get())*30000
    # bumbuprice = int(bumbuEntry.get())*5000
    # gandumprice = int(gandumEntry.get())*20000
    # gulaprice = int(gulaEntry.get())*10000
    # tehprice = int(tehEntry.get())*3000

    totalgroceryprice = HargaBahanBaku1 + HargaBahanBaku2 + HargaBahanBaku3 + HargaBahanBaku4 + HargaBahanBaku5 + HargaBahanBaku6
    totalgrocerytax = totalgroceryprice * 0.10
    set_text(grocertaxEntry, f'Rp. {totalgrocerytax}')
    set_text(grocerpriceEntry, f'Rp. {totalgroceryprice}')

    # # cold drink price calcutaion
    # Penambahan variable harga
    HargaMinuman1 = 0
    HargaMinuman2 = 0
    HargaMinuman3 = 0
    HargaMinuman4 = 0
    HargaMinuman5 = 0
    HargaMinuman6 = 0
    
    # Masukan/Pengahapusan ke Produk List  
    if int(fantaEntry.get()) != 0:
        if ProdukList.validasiproduk('Fanta') == True : ProdukList.tambah_akhir_list('Fanta', 25000, 'Minuman')
        ProdukList.pesanan('Fanta', int(fantaEntry.get()))
        HargaMinuman1 += ProdukList.detailPesanan('Fanta', 'Harga')*ProdukList.detailPesanan('Fanta', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Fanta') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Fanta')
        HargaMinuman1 = 0
    if int(powerfEntry.get()) != 0:
        if ProdukList.validasiproduk('Power F') == True : ProdukList.tambah_akhir_list('Power F', 1500, 'Minuman')
        ProdukList.pesanan('Power F', int(powerfEntry.get()))
        HargaMinuman2 += ProdukList.detailPesanan('Power F', 'Harga')*ProdukList.detailPesanan('Power F', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Power F') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Power F')
        HargaMinuman2 = 0
    if int(spriteEntry.get()) != 0:
        if ProdukList.validasiproduk('Sprite') == True : ProdukList.tambah_akhir_list('Sprite', 5000, 'Minuman')
        ProdukList.pesanan('Sprite', int(spriteEntry.get()))
        HargaMinuman3 += ProdukList.detailPesanan('Sprite', 'Harga')*ProdukList.detailPesanan('Sprite', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Sprite') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Sprite')
        HargaMinuman3 = 0
    if int(pepsiEntry.get()) != 0:
        if ProdukList.validasiproduk('Pepsi') == True : ProdukList.tambah_akhir_list('Pepsi', 2000, 'Minuman')
        ProdukList.pesanan('Pepsi', int(pepsiEntry.get()))
        HargaMinuman4 += ProdukList.detailPesanan('Pepsi', 'Harga')*ProdukList.detailPesanan('Pepsi', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Pepsi') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Pepsi')
        HargaMinuman4 = 0
    if int(cocacolaEntry.get()) != 0:
        if ProdukList.validasiproduk('Coca Cola') == True : ProdukList.tambah_akhir_list('Coca Cola', 10000, 'Minuman')
        ProdukList.pesanan('Coca Cola', int(cocacolaEntry.get()))
        HargaMinuman5 += ProdukList.detailPesanan('Coca Cola', 'Harga')*ProdukList.detailPesanan('Coca Cola', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Coca Cola') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Coca Cola')
        HargaMinuman5 = 0
    if int(kratindengEntry.get()) != 0:
        if ProdukList.validasiproduk('Kratindeng') == True : ProdukList.tambah_akhir_list('Kratindeng', 3000, 'Minuman')
        ProdukList.pesanan('Kratindeng', int(kratindengEntry.get()))
        HargaMinuman6 += ProdukList.detailPesanan('Kratindeng', 'Harga')*ProdukList.detailPesanan('Kratindeng', 'Jumlah')
    else:
        if ProdukList.validasiproduk('Kratindeng') == False : ProdukList.hapus_list_berdasarkan_nama_Produk('Kratindeng')
        HargaMinuman6 = 0

    # print()
    # print('List Produk')
    # ProdukList.cetak_list()
    # fantaprice = int(fantaEntry.get())*25000
    # powerfprice = int(powerfEntry.get())*30000
    # spriteprice = int(spriteEntry.get())*5000
    # pepsiprice = int(pepsiEntry.get())*20000
    # cocacolaprice = int(cocacolaEntry.get())*10000
    # kratindengprice = int(kratindengEntry.get())*3000

    totalcolddrinkprice = HargaMinuman1 + HargaMinuman2 + HargaMinuman3 + HargaMinuman4 + HargaMinuman5 + HargaMinuman6
    totalcolddrinktax = totalcolddrinkprice * 0.1
    set_text(drinktaxEntry, f'Rp. {totalcolddrinktax}')
    set_text(drinkpriceEntry, f'Rp. {totalcolddrinkprice}')


 
def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '' :
        messagebox.showerror('Error', 'Detail Pelanggan diperlukan')
    elif cosmenticpriceEntry.get() == '' or grocerpriceEntry.get() == '' or drinkpriceEntry.get() == '' :
        messagebox.showerror('Error', 'Tidak ada Produk yang dibeli')
    else:
        textarea.delete(1.0, END)

        textarea.insert(END, '======================Selamat datang pelanggan=====================\n')
        textarea.insert(END, f'\n No. Tagihan: {billnumber} \n')
        textarea.insert(END, f'\n Nama Pelanggan: {nameEntry.get()} \n')
        textarea.insert(END, f'\n No. HP Pelanggan: {phoneEntry.get()} \n')
        textarea.insert(END, '\n===================================================================\n')
        textarea.insert(END, f' Produk\t\t\t     Kuantitas\t\t\t\t  Harga')
        textarea.insert(END, '\n===================================================================\n')


        #Cosmetic
        if ProdukList.cekPesanan('Sabun Mandi') == True:
            textarea.insert(END, f' Sabun Mandi     \t\t\t\t{ProdukList.detailPesanan("Sabun Mandi", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Sabun Mandi", "Harga")}\n')
        if ProdukList.cekPesanan('Sabun Wajah') == True:
            textarea.insert(END, f' Sabun Wajah     \t\t\t\t{ProdukList.detailPesanan("Sabun Wajah", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Sabun Wajah", "Harga")}\n')
        if ProdukList.cekPesanan('Parfum') == True:
            textarea.insert(END, f' Parfum     \t\t\t\t{ProdukList.detailPesanan("Parfum", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Parfum", "Harga")}\n')
        if ProdukList.cekPesanan('Sampo') == True:
            textarea.insert(END, f' Sampo     \t\t\t\t{ProdukList.detailPesanan("Sampo", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Sampo", "Harga")}\n')
        if ProdukList.cekPesanan('Skincare') == True:
            textarea.insert(END, f' Skincare     \t\t\t\t{ProdukList.detailPesanan("Skincare", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Skincare", "Harga")}\n')
        if ProdukList.cekPesanan('Autan') == True:
            textarea.insert(END, f' Autan     \t\t\t\t{ProdukList.detailPesanan("Autan", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Autan", "Harga")}\n')

        # if soapprice != 0:
        #     textarea.insert(END, f' Sabun Mandi     \t\t\t\t{bathsoapEntry.get()}\t\t\tRp. {soapprice}\n')
        # if facescreamprice != 0 :
        #     textarea.insert(END, f' Sabun Wajah     \t\t\t\t{facescreamEntry.get()}\t\t\tRp. {facescreamprice}\n')
        # if fashwashprice != 0 :
        #     textarea.insert(END, f' Parfum          \t\t\t\t{fashwashEntry.get()}\t\t\tRp. {fashwashprice}\n')
        # if hairsprayprice != 0 :
        #     textarea.insert(END, f' Sampo           \t\t\t\t{hairsprayEntry.get()}\t\t\tRp. {hairsprayprice}\n')
        # if hairgelprice != 0 :
        #     textarea.insert(END, f' Skincare        \t\t\t\t{hairgelEntry.get()}\t\t\tRp. {hairgelprice}\n')
        # if bodylotionprice != 0 :
        #     textarea.insert(END, f' Autan           \t\t\t\t{bodylotionEntry.get()}\t\t\tRp. {bodylotionprice}\n')
        
        #Grocery
        if ProdukList.cekPesanan('Nasi') == True:
            textarea.insert(END, f' Nasi     \t\t\t\t{ProdukList.detailPesanan("Nasi", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Nasi", "Harga")}\n')
        if ProdukList.cekPesanan('Minyak') == True:
            textarea.insert(END, f' Minyak     \t\t\t\t{ProdukList.detailPesanan("Minyak", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Minyak", "Harga")}\n')
        if ProdukList.cekPesanan('Bumbu') == True:
            textarea.insert(END, f' Bumbu     \t\t\t\t{ProdukList.detailPesanan("Bumbu", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Bumbu", "Harga")}\n')
        if ProdukList.cekPesanan('Gandum') == True:
            textarea.insert(END, f' Gandum     \t\t\t\t{ProdukList.detailPesanan("Gandum", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Gandum", "Harga")}\n')
        if ProdukList.cekPesanan('Gula') == True:
            textarea.insert(END, f' Gula     \t\t\t\t{ProdukList.detailPesanan("Gula", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Gula", "Harga")}\n')
        if ProdukList.cekPesanan('Teh') == True:
            textarea.insert(END, f' Teh     \t\t\t\t{ProdukList.detailPesanan("Teh", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Teh", "Harga")}\n')
        # if riceprice != 0:
        #     textarea.insert(END, f' Beras           \t\t\t\t{riceEntry.get()}\t\t\tRp. {riceprice}\n')
        # if oilprice != 0 :
        #     textarea.insert(END, f' Minyak          \t\t\t\t{oilEntry.get()}\t\t\tRp. {oilprice}\n')
        # if bumbuprice != 0 :
        #     textarea.insert(END, f' Bumbu           \t\t\t\t{bumbuEntry.get()}\t\t\tRp. {bumbuprice}\n')
        # if gandumprice != 0 :
        #     textarea.insert(END, f' Gandum          \t\t\t\t{gandumEntry.get()}\t\t\tRp. {gandumprice}\n')
        # if gulaprice != 0 :
        #     textarea.insert(END, f' Gula            \t\t\t\t{gulaEntry.get()}\t\t\tRp. {gulaprice}\n')
        # if tehprice != 0 :
        #     textarea.insert(END, f' Teh             \t\t\t\t{tehEntry.get()}\t\t\tRp. {tehprice}\n')

        #ColdDrink
        if ProdukList.cekPesanan('Fanta') == True:
            textarea.insert(END, f' Fanta     \t\t\t\t{ProdukList.detailPesanan("Fanta", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Fanta", "Harga")}\n')
        if ProdukList.cekPesanan('Power F') == True:
            textarea.insert(END, f' Power F     \t\t\t\t{ProdukList.detailPesanan("Power F", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Power F", "Harga")}\n')
        if ProdukList.cekPesanan('Sprite') == True:
            textarea.insert(END, f' Sprite     \t\t\t\t{ProdukList.detailPesanan("Sprite", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Sprite", "Harga")}\n')
        if ProdukList.cekPesanan('Pepsi') == True:
            textarea.insert(END, f' Pepsi     \t\t\t\t{ProdukList.detailPesanan("Pepsi", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Pepsi", "Harga")}\n')
        if ProdukList.cekPesanan('Coca Cola') == True:
            textarea.insert(END, f' Coca Cola     \t\t\t\t{ProdukList.detailPesanan("Coca Cola", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Coca Cola", "Harga")}\n')
        if ProdukList.cekPesanan('Kratindeng') == True:
            textarea.insert(END, f' Kratindeng     \t\t\t\t{ProdukList.detailPesanan("Kratindeng", "Jumlah")}\t\t\tRp. {ProdukList.detailPesanan("Kratindeng", "Harga")}\n')
        # if fantaprice != 0:
        #     textarea.insert(END, f' Fanta           \t\t\t\t{fantaEntry.get()}\t\t\tRp. {fantaprice}\n')
        # if powerfprice != 0 :
        #     textarea.insert(END, f' Power F         \t\t\t\t{powerfEntry.get()}\t\t\tRp. {powerfprice}\n')
        # if spriteprice != 0 :
        #     textarea.insert(END, f' Sprite          \t\t\t\t{spriteEntry.get()}\t\t\tRp. {spriteprice}\n')
        # if pepsiprice != 0 :
        #     textarea.insert(END, f' Pepsi           \t\t\t\t{pepsiEntry.get()}\t\t\tRp. {pepsiprice}\n')
        # if cocacolaprice != 0 :
        #     textarea.insert(END, f' Cocacola        \t\t\t\t{cocacolaEntry.get()}\t\t\tRp. {cocacolaprice}\n')
        # if kratindengprice != 0 :   
        #     textarea.insert(END, f' Kratindeng      \t\t\t\t{kratindengEntry.get()}\t\t\tRp. {kratindengprice}\n')

        textarea.insert(END, '\n===================================================================')


        if cosmentictaxEntry.get() != 'Rp. 0.0' :
            textarea.insert(END, f'\n Pajak Kosmetik  \t\t\t\t\t\t{cosmentictaxEntry.get()}')
        if grocertaxEntry.get() != 'Rp. 0.0' :
            textarea.insert(END, f'\n Pajak Bahan baku\t\t\t\t\t\t{grocertaxEntry.get()}')
        if drinktaxEntry.get() != 'Rp. 0.0' :
            textarea.insert(END, f'\n Pajak Minuman   \t\t\t\t\t\t{drinktaxEntry.get()}')

        textarea.insert(END, '\n===================================================================')
        totalbill=totalcosmeticprice+totalgroceryprice+totalcolddrinkprice+totalcosmetictax+totalgrocerytax+totalcolddrinktax
        textarea.insert(END, f'\n Total Tagihan   \t\t\t\t\t\tRP. {totalbill}')
        textarea.insert(END, '\n===================================================================')

        save_bill()


root=Tk()
root.title('System Manajemen Retail')
root.geometry('1300x600')
root.resizable(False, False)
root.configure(background=const.dark)
root.iconbitmap(f'{const.PATHPARENTFILE}/icon.ico')
headingLabel = Label(root, text='System Manajemen Retail', font=('Arial',24,'bold')
                     ,bg=const.primary, fg=const.light, bd=5, relief=RIDGE)
headingLabel.pack(fill=X, pady=10)

customer_details_frame=LabelFrame(root, text='Detail Pelanggan', font=('Arial', 12, 'bold')
                                  ,fg=const.light, bg=const.primary)
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame, text='Nama', font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
nameLabel.grid(row=0, column=0, padx=18, pady=5)

nameEntry=Entry(customer_details_frame, font=('Arial', 12), bd=7, width=25)
nameEntry.grid(row=0,column=1, padx=5, pady=5)

phoneLabel=Label(customer_details_frame, text='No. HP', font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
phoneLabel.grid(row=0, column=2, padx=18, pady=5)

phoneEntry=Entry(customer_details_frame, font=('Arial', 12), bd=7, width=25)
phoneEntry.grid(row=0,column=3, padx=5, pady=5)

billnumberLabel=Label(customer_details_frame, text='No. Tagihan', font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
billnumberLabel.grid(row=0, column=4, padx=18, pady=5)

billnumberEntry=Entry(customer_details_frame, font=('Arial', 12), bd=7, width=25)
billnumberEntry.grid(row=0,column=5, padx=5, pady=5)

searchButton=Button(customer_details_frame, text='Cari', font=('arial', 12, 'bold'), bd='5', width=10, command=search_bill)
searchButton.grid(row=0,column=6,padx=20, pady=5)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame, text='Kosmetik', font=('Arial', 12, 'bold')
                                  ,fg=const.light, bg=const.primary)
cosmeticsFrame.grid(row=0, column=0, pady=3)

bathsoapLabel = Label(cosmeticsFrame, text="Sabun Mandi", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')


bathsoapEntry = Entry(cosmeticsFrame, textvariable='Sabun Mandi', font=('Arial', 12), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1, padx=10)
bathsoapEntry.insert(0, 0)

facescreamLabel = Label(cosmeticsFrame, text="Sabun Wajah", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
facescreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

facescreamEntry = Entry(cosmeticsFrame, textvariable='Sabun Wajah', font=('Arial', 12), width=10, bd=5)
facescreamEntry.grid(row=1, column=1, padx=10)
facescreamEntry.insert(0, 0)

fashwashLabel = Label(cosmeticsFrame, text="Parfum", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
fashwashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

fashwashEntry = Entry(cosmeticsFrame, textvariable='Parfum', font=('Arial', 12), width=10, bd=5)
fashwashEntry.grid(row=2, column=1, padx=10, sticky='w')
fashwashEntry.insert(0, 0)

hairsprayLabel = Label(cosmeticsFrame, text="Sampo", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

hairsprayEntry = Entry(cosmeticsFrame, textvariable='Sampo', font=('Arial', 12), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1, padx=10, sticky='w')
hairsprayEntry.insert(0, 0
                      )
hairgelLabel = Label(cosmeticsFrame, text="Skincare", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

hairgelEntry = Entry(cosmeticsFrame, textvariable='Skincare',  font=('Arial', 12), width=10, bd=5)
hairgelEntry.grid(row=4, column=1, padx=10, sticky='w')
hairgelEntry.insert(0, 0)

bodylotionLabel = Label(cosmeticsFrame, text="Autan", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

bodylotionEntry = Entry(cosmeticsFrame, textvariable='Autan', font=('Arial', 12), width=10, bd=5)
bodylotionEntry.grid(row=5, column=1, padx=10, sticky='w')
bodylotionEntry.insert(0, 0)


groceryFrame=LabelFrame(productsFrame, text='Bahan baku', font=('Arial', 12, 'bold')
                                  ,fg=const.light, bg=const.primary)
groceryFrame.grid(row=0, column=1, pady=3)

riceLabel = Label(groceryFrame, text="Nasi", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

riceEntry = Entry(groceryFrame, font=('Arial', 12), width=10, bd=5)
riceEntry.grid(row=0, column=1, padx=10)
riceEntry.insert(0, 0)

oilLabel = Label(groceryFrame, text="Minyak", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

oilEntry = Entry(groceryFrame, font=('Arial', 12), width=10, bd=5)
oilEntry.grid(row=1, column=1, padx=10)
oilEntry.insert(0, 0)

bumbuLabel = Label(groceryFrame, text="Bumbu", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
bumbuLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

bumbuEntry = Entry(groceryFrame, font=('Arial', 12), width=10, bd=5)
bumbuEntry.grid(row=2, column=1, padx=10, sticky='w')
bumbuEntry.insert(0, 0)

gandumLabel = Label(groceryFrame, text="Gandum", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
gandumLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

gandumEntry = Entry(groceryFrame, font=('Arial', 12), width=10, bd=5)
gandumEntry.grid(row=3, column=1, padx=10, sticky='w')
gandumEntry.insert(0, 0)

gulaLabel = Label(groceryFrame, text="Gula", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
gulaLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

gulaEntry = Entry(groceryFrame, font=('Arial', 12), width=10, bd=5)
gulaEntry.grid(row=4, column=1, padx=10, sticky='w')
gulaEntry.insert(0, 0)

tehLabel = Label(groceryFrame, text="Teh", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
tehLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

tehEntry = Entry(groceryFrame, font=('Arial', 12), width=10, bd=5)
tehEntry.grid(row=5, column=1, padx=10, sticky='w')
tehEntry.insert(0, 0)


colddrinkFrame=LabelFrame(productsFrame, text='Minuman', font=('Arial', 12, 'bold')
                                  ,fg=const.light, bg=const.primary)
colddrinkFrame.grid(row=0, column=2, pady=3)

fantaLabel = Label(colddrinkFrame, text="Fanta", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
fantaLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

fantaEntry = Entry(colddrinkFrame, font=('Arial', 12), width=10, bd=5)
fantaEntry.grid(row=0, column=1, padx=10)
fantaEntry.insert(0, 0)

powerfLabel = Label(colddrinkFrame, text="Power F", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
powerfLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

powerfEntry = Entry(colddrinkFrame, font=('Arial', 12), width=10, bd=5)
powerfEntry.grid(row=1, column=1, padx=10)
powerfEntry.insert(0, 0)

spriteLabel = Label(colddrinkFrame, text="Sprite", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
spriteLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

spriteEntry = Entry(colddrinkFrame, font=('Arial', 12), width=10, bd=5)
spriteEntry.grid(row=2, column=1, padx=10, sticky='w')
spriteEntry.insert(0, 0)

pepsiLabel = Label(colddrinkFrame, text="Pepsi", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
pepsiLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

pepsiEntry = Entry(colddrinkFrame, font=('Arial', 12), width=10, bd=5)
pepsiEntry.grid(row=3, column=1, padx=10, sticky='w')
pepsiEntry.insert(0, 0)

cocacolaLabel = Label(colddrinkFrame, text="Coca Cola", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
cocacolaLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

cocacolaEntry = Entry(colddrinkFrame, font=('Arial', 12), width=10, bd=5)
cocacolaEntry.grid(row=4, column=1, padx=10, sticky='w')
cocacolaEntry.insert(0, 0)

kratindengLabel = Label(colddrinkFrame, text="kratindeng", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
kratindengLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

kratindengEntry = Entry(colddrinkFrame, font=('Arial', 12), width=10, bd=5)
kratindengEntry.grid(row=5, column=1, padx=10, sticky='w')
kratindengEntry.insert(0,0)

billframe=Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

bilareaLabel=Label(billframe, text='Struct Tagihan', font=('Arial', 15, 'bold'), bd=7, relief=GROOVE)
bilareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea=Text(billframe, height=14, width=67, yscrollcommand=scrollbar.set)
textarea.pack(pady=3)

scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root, text='Menu Tagihan', font=('Arial', 12, 'bold')
                                  ,fg=const.light, bg=const.primary)
billmenuFrame.pack()

cosmenticpriceLabel = Label(billmenuFrame, text="Harga Cosmetik", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
cosmenticpriceLabel.grid(row=0, column=0, pady=9, padx=10)

cosmenticpriceEntry = Entry(billmenuFrame, font=('Arial', 12), width=11, bd=5)
cosmenticpriceEntry.grid(row=0, column=1, padx=10, sticky='w')

grocerpriceLabel = Label(billmenuFrame, text="Harga Bahan baku", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
grocerpriceLabel.grid(row=1, column=0, pady=9, padx=10)

grocerpriceEntry = Entry(billmenuFrame, font=('Arial', 12), width=11, bd=5)
grocerpriceEntry.grid(row=1, column=1, padx=10, sticky='w')

drinkpriceLabel = Label(billmenuFrame, text="Harga Minuman", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
drinkpriceLabel.grid(row=2, column=0, pady=9, padx=10)

drinkpriceEntry = Entry(billmenuFrame, font=('Arial', 12), width=11, bd=5)
drinkpriceEntry.grid(row=2, column=1, padx=10, sticky='w')

cosmentictaxLabel = Label(billmenuFrame, text="Pajak Kosmetik", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
cosmentictaxLabel.grid(row=0, column=2, pady=9, padx=10)

cosmentictaxEntry = Entry(billmenuFrame, font=('Arial', 12), width=11, bd=5)
cosmentictaxEntry.grid(row=0, column=3, padx=10, sticky='w')

grocertaxLabel = Label(billmenuFrame, text="Pajak Bahan baku", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
grocertaxLabel.grid(row=1, column=2, pady=9, padx=10)

grocertaxEntry = Entry(billmenuFrame, font=('Arial', 12), width=11, bd=5)
grocertaxEntry.grid(row=1, column=3, padx=10, sticky='w')

drinktaxLabel = Label(billmenuFrame, text="Pajak Minuman", font=('Arial', 12, 'bold'), bg=const.primary, fg=const.light)
drinktaxLabel.grid(row=2, column=2, pady=9, padx=10)

drinktaxEntry = Entry(billmenuFrame, font=('Arial', 12), width=11, bd=5)
drinktaxEntry.grid(row=2, column=3, padx=10, sticky='w')

buttomFrame=Frame(billmenuFrame, bd=8, relief=GROOVE)
buttomFrame.grid(row=0, column=4, rowspan=3)

totalButton=Button(buttomFrame, text='Total', font=('Arial', 14 , 'bold'), bg=const.primary, fg=const.light, bd=5,width=10, pady=10, command=total)
totalButton.grid(row=6, column=0, pady=20, padx=5)

tagihanButton=Button(buttomFrame, text='Tagih', font=('Arial', 14 , 'bold'), bg=const.primary, fg=const.light, bd=5,width=9, pady=10, command=bill_area)
tagihanButton.grid(row=6, column=1, pady=20, padx=5)

emailButton=Button(buttomFrame, text='Email', font=('Arial', 14 , 'bold'), bg=const.primary, fg=const.light, bd=5,width=9, pady=10, command=send_email)
emailButton.grid(row=6, column=2, pady=20, padx=5)

CetakButton=Button(buttomFrame, text='Cetak', font=('Arial', 14 , 'bold'), bg=const.primary, fg=const.light, bd=5,width=9, pady=10, command=print_bill)
CetakButton.grid(row=6, column=4, pady=20, padx=5)

bersihButton=Button(buttomFrame, text='Bersih', font=('Arial', 14 , 'bold'), bg=const.primary, fg=const.light, bd=5,width=9, pady=10, command=clear)
bersihButton.grid(row=6, column=5, pady=20, padx=5)



root.mainloop()