from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Mendefinisikan fungsi salam
# Logging dengan history yang terecord di salam.txt
# Loggingnya dishow di website (og)

def salam_user(nama):
    if nama.lower() == "hafiz":
        return "Halo master!, kamu sudah datang, silahkan!"
    else:
        return "Halo, " + nama + "! selamat datang ke situsku"

@app.route('/', methods=['GET', 'POST'])
def home():
    pesan = ""  # Temporary variable for greeting
    salam_history = []  # List to store existing greetings from the file

    # Membaca salam existing dari file, di luar block POST
    try:
        with open("salam.txt", "r") as file:
            salam_history = file.readlines()
    except FileNotFoundError:
        salam_history = []  # If file doesn't exist yet, start with empty list

    if request.method == 'POST':
        nama = request.form.get('nama', '')  # Dapatkan nama dari form
        if nama:
            pesan = salam_user(nama)
            # Menyimpan salam ke dalam file
            with open("salam.txt", "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}] {pesan}\n")
            # Re-read the file to include the new entry
            with open("salam.txt", "r") as file:
                salam_history = file.readlines()
            print(salam_history)  # Debug output

    print("Rendering with:", salam_history)  # Add this line
    return render_template('index.html', message=pesan, salam_history=salam_history)

if __name__ == '__main__':
    app.run(debug=True, port=5001)