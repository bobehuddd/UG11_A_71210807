def calculator():
    print("======== Calculator sederhana ========")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    pilih= int(input("Masukkan pilihan: "))
    if pilih==1 :
        tambah()
    elif pilih==2:
        kurang()
    elif pilih==3:
        kali()
    elif pilih==4:
        bagi()
    elif pilih==5:
        pangkat()
    else :
        print("Maaf input operasi antara 1-5")

    return calculator()

def tambah():
    num_1=int(input("Masukkan bilangan 1: "))
    num_2=int(input("Masukkan bilangan 2: "))
    total=num_1+num_2
    print("Hasilnya :",total)

def kurang():
    num_1=int(input("Masukkan bilangan 1: "))
    num_2=int(input("Masukkan bilangan 2: "))
    total=num_1-num_2
    print("Hasilnya :",total)

def kali():
    num_1=int(input("Masukkan bilangan 1: "))
    num_2=int(input("Masukkan bilangan 2: "))
    total=num_1*num_2
    print("Hasilnya :",total)

def bagi():
    num_1=int(input("Masukkan bilangan 1: "))
    num_2=int(input("Masukkan bilangan 2: "))
    total=num_1/num_2
    print("Hasilnya :",total)

def pangkat():
    num_1=int(input("Masukkan bilangan 1: "))
    num_2=int(input("Masukkan bilangan 2: "))
    total=num_1**num_2
    print("Hasilnya :",total)

calculator()