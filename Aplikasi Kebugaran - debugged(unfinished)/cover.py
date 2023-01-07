import os
import login

def splashCover():
    # Clearing the Screen
    os.system('cls')

    #di bagian ini silakan berlomba-lomba membuat tampilan splash yang menarik
    #gunakan fungsi iterasi/lopping
    for i in range (1, 40):
        print("= ",end="")
    print()
    for i in range (1, 40):
        print(" ⨯",end="")
    print()
    for i in range (1, 40):
        print("= ",end="")



    print("""
 ██████  ███    ██ ███████ ███████ ██ ████████      █████  ██████  ██████  
██    ██ ████   ██ ██      ██      ██    ██        ██   ██ ██   ██ ██   ██ 
██    ██ ██ ██  ██ █████   █████   ██    ██        ███████ ██████  ██████  
██    ██ ██  ██ ██ ██      ██      ██    ██        ██   ██ ██      ██      
 ██████  ██   ████ ███████ ██      ██    ██        ██   ██ ██      ██      
    """)
    for i in range (1, 40):
        print("⨯ ",end="")
    print()
    for i in range (1, 40):
        print(" =",end="")
    print()
    for i in range (1, 40):
        print("⨯ ",end="")
    print ()

def closing():
    print("Terimakasih anda telah menggunakan aplikasi kami")
    print('onefit app v 1.0.0')
    quit()

def pilihan():
    while True:
        pilihan = input("Silakan ketikan m untuk melanjutkan kedalam aplikasi dan k untuk keluar\n")
        if(pilihan == "m"):
            print("Selamat datang di aplikasi OneFit \n silahkan login untuk melanjutkan")
            login.home_login()
            # lanjut ke bagian login
            break
        elif(pilihan == "k"):
            print("Anda akan keluar dari aplikasi")
            # keluar dari aplikasi
            break
        else:
            print("Input invalid. Mohon ketikkan M atau K saja")
