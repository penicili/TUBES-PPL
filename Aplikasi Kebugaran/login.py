import os
import transaksi_utama
import getpass

def home_login():
    # Clearing the Screen
    os.system('cls')
    # Requesting login data
    
    print("Silakan login untuk melanjutkan kedalam aplikasi")
    while True:
        username = (input("Silakan masukan username\n"))
        print ('Silahkan masukkan password')
        password = getpass.getpass('(Password yang anda ketikkan tidak akan muncul pada layar anda)\n')
        status_auth = check_autentifikasi(username, password)
        if(status_auth == True):
            transaksi_utama.transaksi()
            # lanjut ke main menu
            break
        else:
            print('Username atau password yang anda masukkan salah')
            print('Silahkan coba lagi\n')
        
def check_autentifikasi(_username, _password):
    #untuk sementara checkingnya hardcoded
    username1 = "admin"
    password1 = "telkom"
    if(_username == username1 and _password == password1):
        print("Username dan password anda benar")
        return True
    else:
        os.system('cls')
        return False