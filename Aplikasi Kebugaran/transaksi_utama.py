# Transksi utama (main menu)
import os
import math

def transaksi():
     # Clearing the Screen
    os.system('cls')
    print ("""
Berhasil login!

  __  __                       _    _  _                           
 |  \/  |                     | |  | || |                          
 | \  / |  ___  _ __   _   _  | |  | || |_  __ _  _ __ ___    __ _ 
 | |\/| | / _ \| '_ \ | | | | | |  | || __|/ _` || '_ ` _ \  / _` |
 | |  | ||  __/| | | || |_| | | |__| || |_| (_| || | | | | || (_| |
 |_|  |_| \___||_| |_| \__,_|  \____/  \__|\__,_||_| |_| |_| \__,_|


1.) Hitung BMI
2.) Hitung kalori dari makanan
3.) Hitung kalori yang terbakar                                                           
                                                                                            onefit version 1.0.0
    """)
    # meminta input user
    menuSelect = int (input('Masukkan pilihan sesuai dengan pilihan yang disediakan\n'))
    
    # mengeksekusi perintah sesuai input user
    if menuSelect == 1:
        bodyWeight = int (input('Masukkan berat badan anda dalam kilogram\n'))
        bodyTall = int (input('Masukkan tinggi badan anda dalam sentimeter\n'))
        bmi = BmiCount(bodyWeight, bodyTall)
        bmiStatus = BmiIf(bmi)
        normalBmi = '18.5 - 24.9'
        if bmi < 18.5:
            berat = 'dibawah ideal'
            tallCm = bodyTall/100
            idealberat = (tallCm ** 2)*18.5
            idealberat = round(idealberat,1)
        elif bmi > 24.9 and bmi < 30:
            berat = 'diatas ideal'
            tallCm = bodyTall/100
            idealberat = (tallCm ** 2)*24.9
            idealberat = round(idealberat,1)
        elif bmi > 30:
            berat = 'Obesitas'
            tallCm = bodyTall/100
            idealberat = (tallCm ** 2)*24.9
            idealberat = round(idealberat,1)
        else:
            berat = 'Ideal'
            idealberat = 'sudah tercapai, atur pola makan dan olahraga teratur untuk menjaga berat ideal'
        os.system('cls')
        print ( f"""
***onefit BMI counter v 1.0.0***
Berat badan | BMI | Keterangan
     {bodyWeight}     | {bmi} | {bmiStatus}
bmi normal adalah {normalBmi}
""")    
        if berat != 'Ideal':
            print(f'berat tubuh anda {bodyWeight}, berat ideal anda {idealberat} kilogram')
        else:
            print(f'berat tubuh anda{bodyWeight},sudah mencapai berat ideal anda')
            print('===========================================================')
        # Kembali ke main menu
        while True:
            returnOrQuit = input ('Ingin kembali ke main menu?(y/n)')
            if returnOrQuit == 'y':
                transaksi ()
                break
            elif returnOrQuit =='n':
                break
            else:
                print ('Harap masukkan input dengan sesuai')
    # user memilih menu 2
    elif menuSelect == 2:
        foodlist =[]
        calorList= []
        foodjmlhlist= []
        totalCal = 0
        k = 0
        x = 0
        # meminta input user
        while True:
            k  += 1
            print("""
***Harap masukkan jenis makanan***
1.) Nasi
2.) Ayam Goreng
3.) Telur
            """)
            food = input('')
            if food == '1':
                foodAmount = int(input ('Berapa centong nasi?\n'))
                foodbanyak = str(foodAmount)
                foodJmlh = (foodbanyak + ' Centong')
                foodkind = 'Nasi'
            elif food == '2':
                foodAmount = int(input ('Berapa potong ayam goreng?\n'))
                foodbanyak = str(foodAmount)
                foodJmlh = (foodbanyak + ' potong')
                foodkind = 'Ayam goreng'
            elif food == '3':
                foodAmount = int(input ('Berapa butir telur?\n'))
                foodbanyak = str(foodAmount)
                foodJmlh = (foodbanyak + ' butir')
                foodkind = 'Telur'
            else:
                print ('Input yang dimasukkan invalid, mohon tulis angka sesuai pilihan yang disediakan')
                continue
            calories = foodCount(food,foodAmount)
            foodlist.append(foodkind)
            calorList.append(calories)
            foodjmlhlist.append(foodJmlh)
            intcal = int (calories)
            totalCal += intcal
            inputAgain = input('Apakah anda ingin menambahkan makanan lain (y/n)')
            if inputAgain == 'y':
                pass
            elif inputAgain == 'n':
                break
            # hasil hitung
        print ('\n=========onefit calorie counter v 1.0.0=========\n Nama makanan | Jumlah | Kalori yang masuk')
        k2 = 0
        while k >k2:
            k2 += 1
            print(foodlist[x], "|", foodjmlhlist[x], "|" , calorList[x], 'kcal')
            x += 1
        print ('Kalori total: ', totalCal,'kcal')
        # Kembali ke main menu
        while True:
            returnOrQuit = input ('Ingin kembali ke main menu?(y/n)')
            if returnOrQuit == 'y':
                transaksi ()
                break
            elif returnOrQuit =='n':
                break
            else:
                print ('Harap masukkan input dengan sesuai')        

    elif menuSelect == 3:
        sportlist =[]
        burnList= []
        sportjmlhlist= []
        totalBurnt = 0
        k = 0
        x = 0
        # meminta input user
        while True:
            k  += 1
            print("""
***Harap masukkan jenis olahraga***
1.) Lari
2.) Bersepeda
            """)
            sport = input('')
            if sport == '1':
                sportAmount = int(input ('Lari berapa kilometer?\n'))
                sportbanyak = str(sportAmount)
                sportJmlh = (sportbanyak + ' kilometer')
                sportkind = 'Lari'
            if sport == '2':
                sportAmount = int(input ('Bersepeda berapa Jam?\n'))
                sportbanyak = str(sportAmount)
                sportJmlh = (sportbanyak + ' Jam')
                sportkind = 'Jam'
            # else:
            #     print ('Input yang dimasukkan invalid, mohon tulis angka sesuai pilihan yang disediakan')
            #     continue
            caloriesBurnt = sportCount(sport,sportAmount)
            sportlist.append(sportkind)
            burnList.append(caloriesBurnt)
            sportjmlhlist.append(sportJmlh)
            intburnt = int (caloriesBurnt)
            totalBurnt += intburnt
            inputAgain = input('Apakah anda ingin menambahkan olahraga lain (y/n)')
            if inputAgain == 'y':
                pass
            elif inputAgain == 'n':
                break
            # hasil hitung
        print ('\n=========onefit burnt calorie counter v 1.0.0=========\n Nama Olahraga | Jumlah | Kalori yang terbakar')
        k2 = 0
        while k >k2:
            k2 += 1
            print(sportlist[x], "|", sportjmlhlist[x], "|" , burnList[x], 'kcal')
            x += 1
        print ('Kalori yang terbakar: ', totalBurnt,'kcal')
        # Kembali ke main menu
        while True:
            returnOrQuit = input ('Ingin kembali ke main menu?(y/n)')
            if returnOrQuit == 'y':
                transaksi ()
                break
            elif returnOrQuit =='n':
                break
            else:
                print ('Harap masukkan input dengan sesuai')      
    else:
        transaksi()

def BmiCount(beratBadan,TinggiBadan):
    tinggiMeter = TinggiBadan / 100
    bmi = beratBadan / (tinggiMeter ** 2)
    bmi = round(bmi, 1)
    return bmi
def BmiIf (bmi):
    if bmi < 18.5:
        bmiStatus = 'Kurang'
    elif bmi >= 18.5 and  bmi <= 24.9 :
        bmiStatus = 'Ideal'
    elif bmi > 24.9 and bmi <= 29.9:
        bmiStatus = 'Lebih'
    elif bmi > 29.9:
        bmiStatus = 'Obesitas'

    return bmiStatus

def foodCount(_food,_foodAmount):
    os.system('cls')
    if _food == '1':
        calories = 129 * _foodAmount
    elif _food == '2':
        calories = 246 * _foodAmount
    elif _food == '3':
        calories = 155 * _foodAmount
    return calories

def sportCount(_sport,_sportamount):
    os.system('cls')
    if _sport == '1':
        calories = 380 * _sportamount
    elif _sport == '2':
        calories = 358 * _sportamount
    return calories


    # total_pembayaran = 0
    
    # while(True):
    #     pilihan = int(input("Silakan pilih menu makanan atau 0 untuk keluar"))
    #     if(pilihan == 1):
    #         jumlah = int(input("Masukkan jumlah"))
    #         print("Anda memilih lele goreng jumlahnya ", jumlah)
    #         total = jumlah*15000
    #         total_pembayaran = total_pembayaran + total
    #     elif(pilihan ==2):
    #         pil2 = int(input("Masukkan jumlah"))
    #         print("Anda memilih ayam goreng jumlahnya ", jumlah)
    #         total = jumlah*25000
    #         total_pembayaran = total_pembayaran + total
    #     elif(pilihan ==3):
    #         pil2 = int(input("Masukkan jumlah"))
    #     elif(pilihan ==4):
    #         pil2 = int(input("Masukkan jumlah")) 
    #     elif(pilihan ==0):
    #         #Untuk keluar dari pilihannya
    #         print("Terimakasih pesanan anda telah lengkap")
    #         print("Total Pembayaran anda :", total_pembayaran)
    #         break   
    #     else:
    #         print("Silakan pilih sesuai menu yang ada")
    #         transaksi()
