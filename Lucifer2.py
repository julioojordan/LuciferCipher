# Encryption Decryption Using Lucifer cipher
#Julio Andan Jordan Aryanto
#24060117130078
#DIPONEGORO UNIVERSITY
#IT 17
from tkinter import * 


#inisialisasi
#pembuatan key
def Key(key):
    #porses 1 pembuatan key
    arrayK =[]
    for i in range(len(key)):
        if key[i] != ' ' :
            arrayK.append(key[i])

    #menyimpan key dalam bentuk biner per charakter nya                            
    arrayKbiner =[]
    for i in range(len(arrayK)):
        biner = ''.join(format(ord(j), '08b') for j in arrayK[i])
        arrayKbiner.append(biner)

    #proses 2 pembuatan k0 sampai k15 menggunakan Tkbas
    arraykey = []
    for i in range(len(Tkbas)):
        temp = []
        for j in range(len(Tkbas[i])):
            k = Tkbas[i][j]
            temp.append(arrayKbiner[k])
        join = ''.join(map(str, temp))
        arraykey.append(join)

    return arraykey

def array_int(array):
    array_int = []
    for i in range(len(array)):
        array_int.append(int(array[i]))
    return array_int

#mengubah biner ke decimal
def BinaryToDecimal(binary):  
         
    binary1 = binary  
    decimal, i, n = 0, 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return (decimal)

#Fungsi untuk enkripsi
def Enkripsi():

    plainteks = e1.get()
    key = e2.get()
    #=======Pembuatan key=======
    arraykey = Key(key)
    #======= ENd proses Pembuatan Key =======

    #======= proses enkripsi=======
    arrayR = []
    arrayL = []

    #porses 1 enkripsi menghilangkan spasi input dan menyimpan ke array k per charakter
    arrayP =[]
    for i in range(len(plainteks)):
        if plainteks[i] != ' ' :
            arrayP.append(plainteks[i])

    #proses 2 enkripsi, convert setiap char ke biner dan memasukan
    #8 byte per tama ke L, 8 byte terakhir ke R
    arrayPbiner =[]
    for i in range(len(arrayP)):
        biner = ''.join(format(ord(j), '08b') for j in arrayP[i])
        arrayPbiner.append(biner)
            
    for i in range(len(arrayPbiner)):
        if i <= 7:
            arrayL.append(arrayPbiner[i])
        else:
            arrayR.append(arrayPbiner[i])
                
    L = ''.join(map(str, arrayL)) #untuk menyimpan L
    R = ''.join(map(str, arrayR)) #untuk menyimpan R
    tempL = []
    tempR = []
    tempL.append(L)
    tempR.append(R)

    #proses 3 enkripsi, perhitungan 16 ronde enkripsi lucifer
    for i in range(16):
        Li = tempR[i]
        tempL.append(Li) #memasukan nilai Li+1 = Ri
            
        #menghitung Ri+1 = Li xor f(Ri, Ki)
        bL = array_int(tempL[i])
        bR = array_int(tempR[i])
        bK = array_int(arraykey[i])
            
        #menghitung fungsi f = Ri xor Ki
        tempF = [] #inisialisasi list untuk menyimpan hasil fungsi f
        for j in range(len(bR)):
            add = bR[j] ^ bK[j]
            tempF.append(add)
            
        #menghitung Ri+1
        tempR2 = []
        for j in range(len(bR)):
            add = bL[j] ^ tempF[j]
            tempR2.append(add)
        Ri = ''.join(map(str, tempR2))
        tempR.append(Ri)

        print (i+1)
        print (tempL[i+1])
        print (tempR[i+1])
        #cek apakah dia sudah putaran terakhir atau belum
        if i != 15:
            temp = tempL[i+1]
            tempL[i+1] = tempR[i+1]
            tempR[i+1] = temp

    result_L = tempL[15]
    result_R = tempR[15]
    result = result_L+result_R
    #print(result)
    cipherteks = ''
    binary_values = [result[i:i+8] for i in range(0, len(result), 8)]
    #print(binary_values)
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        cipherteks += ascii_character
    #print(cipherteks)
    e3.insert(0, cipherteks)
#===============END fungsi Enkripsi================

#fungsi untuk dekripsi
def Dekripsi():
    cipherteks = e4.get()
    key = e5.get()
    #=======Pembuatan key=======
    arraykey = Key(key)
    #======= ENd proses Pembuatan Key =======

    #======= proses Dekripsi=======
    arrayR = []
    arrayL = []

    #porses 1 dekripsi menghilangkan spasi input dan menyimpan ke array k per charakter
    arrayC =[]
    for i in range(len(cipherteks)):
        if cipherteks[i] != ' ' :
            arrayC.append(cipherteks[i])

    #proses 2 dekripsi, convert setiap char ke biner dan memasukan
    #8 byte per tama ke L, 8 byte terakhir ke R
    arrayCbiner =[]
    for i in range(len(arrayC)):
        biner = ''.join(format(ord(j), '08b') for j in arrayC[i])
        arrayCbiner.append(biner)
            
    for i in range(len(arrayCbiner)):
        if i <= 7:
            arrayL.append(arrayCbiner[i])
        else:
            arrayR.append(arrayCbiner[i])
                
    L = ''.join(map(str, arrayL)) #untuk menyimpan L
    R = ''.join(map(str, arrayR)) #untuk menyimpan R
    tempL = []
    tempR = []
    tempL.append(L)
    tempR.append(R)

    #proses 3 dekripsi, perhitungan 16 ronde dekripsi lucifer
    for i in range(16):
        Li = tempR[i]
        tempL.append(Li) #memasukan nilai Li+1 = Ri
            
        #menghitung Ri+1 = Li xor f(Ri, Ki)
        bL = array_int(tempL[i])
        bR = array_int(tempR[i])
        bK = array_int(arraykey[i])
            
        #menghitung fungsi f = Ri xor Ki
        tempF = [] #inisialisasi list untuk menyimpan hasil fungsi f
        for j in range(len(bR)):
            add = bR[j] ^ bK[j]
            tempF.append(add)
            
        #menghitung Ri+1
        tempR2 = []
        for j in range(len(bR)):
            add = bL[j] ^ tempF[j]
            tempR2.append(add)
        Ri = ''.join(map(str, tempR2))
        tempR.append(Ri)

        print (i+1)
        print (tempL[i+1])
        print (tempR[i+1])
        #cek apakah dia sudah putaran terakhir atau belum
        if i != 15:
            temp = tempL[i+1]
            tempL[i+1] = tempR[i+1]
            tempR[i+1] = temp

    result_L = tempL[15]
    result_R = tempR[15]
    result = result_L+result_R

    plainteks = ''
    binary_values = [result[i:i+8] for i in range(0, len(result), 8)]
    #print(binary_values)
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        plainteks += ascii_character
    #print(plainteks)
    e6.insert(0, plainteks)
#===========END Dekripsi===========

        
#tabel Key Byte Access Scheldule
Tkbas = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [7, 8, 9, 10, 11, 12, 13, 14],
    [14, 15, 0, 1, 2, 3, 4, 5],
    [5, 6, 7, 8, 9, 10, 11, 12],
    [12, 13, 14, 15, 0, 1, 2, 3],
    [3, 4, 5, 6, 7, 8, 9, 10],
    [10, 11, 12, 13, 14, 15, 0, 1],
    [1, 2, 3, 4, 5 ,6, 7, 8],
    [8, 9, 10, 11, 12, 13, 14, 15],
    [15, 0 , 1, 2 ,3 ,4 ,5 ,6],
    [6, 7, 8, 9, 10, 11, 12, 13],
    [13, 14, 15, 0, 1, 2, 3, 4],
    [4, 5, 6, 7, 8, 9, 10, 11],
    [11, 12, 13 ,14, 15, 0, 1, 2],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 10 ,11, 12, 13, 14, 15, 0],
]

#=======================END INISIALISASI=====================
#mulai
root = Tk() 
root.title("Lucifer Encryption-Decryption") 
root.geometry("800x600")
              
# Label dan posisi 
label1 = Label(root, text ='Plaintext')                
label1.grid(row = 10, column = 1) 
label2 = Label(root, text ='Key') 
label2.grid(row = 11, column = 1) 
label3 = Label(root, text ="Ciphertext") 
label3.grid(row = 12, column = 1)

label4 = Label(root, text ='Ciphertext')                
label4.grid(row = 10, column = 10) 
label5 = Label(root, text ='Key') 
label5.grid(row = 11, column = 10) 
label6 = Label(root, text ="Plaintext") 
label6.grid(row = 12, column = 10)


# membuat input box
e1 = Entry(root) 
e1.grid(row = 10, column = 2) 
e2 = Entry(root) 
e2.grid(row = 11, column = 2) 
e3 = Entry(root) #untuk hasil enkripsi
e3.grid(row = 12, column = 2)

e4 = Entry(root) 
e4.grid(row = 10, column = 11) 
e5 = Entry(root) 
e5.grid(row = 11, column = 11) 
e6 = Entry(root) #untuk hasil dekripsi
e6.grid(row = 12, column = 11)        


#membuat tombol enkripsi    
b1 = Button(root, text = "Encrypt", bg ="red", fg ="white", command = Enkripsi) 
b1.grid(row = 14, column = 2)       


#membuat tombol enkripsi    
b2 = Button(root, text = "Decrypt", bg ="green", fg ="white", command = Dekripsi) 
b2.grid(row = 14, column = 11)

