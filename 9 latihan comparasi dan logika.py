# Latihan Logika dan Komparasi

# Membuat rentang gabungan area dari angka

#++++++3-----10+++++

InputUser = float(input("Masukkan angka yang bernilai \n kurang dari 3 \n atau \n lebih dari 10:"))

#Memeriksa angka kurang dari 3
#+++++++++++3-----------------

isKurangDari = (InputUser < 3)
print ("Kurang dari 3 =", isKurangDari) 

#Memeriksa angka lebih dari 10
#+++++++++++3-----------------

isLebihDari = (InputUser > 10)
print ("Lebih dari 10 =", isLebihDari) 

#++++++++3-------10++++++++

IsCorrect = isKurangDari or isLebihDari
print ("Angka yang anda masukkan: ", IsCorrect)

#-----3++++++10------
print ("\n", 10*"=","\n")

InputUser = float(input("Masukkan angka yang bernilai \n lebih dari 3 \n dan \n kurang dari 10:"))

#Memeriksa angka lebih dari 3
#--------3++++++++++

isLebihDari = (InputUser > 3)
print ("Lebih dari 3 =", isLebihDari) 

#Memeriksa angka kurang dari 10
#-------10++++++++

isKurangDari = (InputUser < 10)
print ("Kurang dari 10 =", isKurangDari) 

#++++++++3-------10++++++++

IsCorrect = isKurangDari and isLebihDari
print ("Angka yang anda masukkan: ", IsCorrect)
