# mendefinisikan fungsi untuk menciptakan ucapan selamat
def salam_user(nama):
    if nama.lower() == "hafiz": #case sensitive check
        return "Halo, kami sudah menunggumu! " + nama + " selamat datang di sini!"
    else:
        return "Halo, " + nama + " selamat datang di sini!"
    
# menanyakan nama
nama = input("masukkan namamu : ")

# memanggil fungsi dan mengeluarkan hasilnya
pesan = salam_user(nama)
print(pesan)    