# mendefinisikan fungsi untuk menciptakan ucapan selamat
def salam_user(nama):
    if nama.lower() == "hafiz": #case sensitive check
        return "Halo, kami sudah menunggumu! " + nama + " selamat datang di sini!"
    else:
        return "Halo, " + nama + " selamat datang di sini!"
    


#buka file dan mencoba log salamnya tadi

with open("salam.txt", "a") as file:
    #with open("greetings.txt", "a"): Opens a file in “append” mode to save greetings.
    while True:
        # menanyakan nama
        nama = input("masukkan namamu (atau ketik 'quit' untuk keluar)\n nama: ")
        if nama.lower() == "quit":
            break #keluar loop

        # memanggil fungsi dan mengeluarkan hasilnya
        pesan = salam_user(nama)
        print(pesan)    

        #menyimpan pesan salam ke dalam file
        file.write(pesan + "\n")

print("Salam tersimpan ke dalam salam.txt")
