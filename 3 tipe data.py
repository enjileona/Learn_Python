
#belajar casting data
#merubah dari satu tipe ke tipe yang lain
#tipe data: string, integer, float, boolean

##integer
print("======INTEGER======")
data_int = 9;
print ("data =", data_int, ",type = ", type (data_int))

data_float   = float (data_int)
data_str     = str (data_int)
data_bool    = bool (data_int)
print ("data =", data_float, ",type = ", type (data_float))
print ("data =", data_str, ",type = ", type (data_str))
print ("data =", data_bool, ",type = ", type (data_bool)) #akan false jika nilai int=0

##float
print("=======FLOAT======")
data_float   = 9.5;
print ("data =", data_float, ",type = ", type (data_float))

data_int     = int (data_float) #akan dibulatkan kebawah
data_str     = str (data_float)
data_bool    = bool (data_float)
print ("data =", data_int, ",type = ", type (data_int))
print ("data =", data_str, ",type = ", type (data_str))
print ("data =", data_bool, ",type = ", type (data_bool)) #akan false jika nilai float = 0

##boolean
print("=======BOOLEAN======")
data_bool   = True;
print ("data =", data_bool, ",type = ", type (data_bool))

data_int     = int (data_bool) #akan dibulatkan kebawah
data_str     = str (data_bool)
data_float   = float (data_bool)
print ("data =", data_int, ",type = ", type (data_int))
print ("data =", data_str, ",type = ", type (data_str))
print ("data =", data_float, ",type = ", type (data_float)) #akan false jika nilai float = 0

##string
print("=======STRING======")
data_string   = "10";
print ("data =", data_string, ",type = ", type (data_string))

data_int     = int (data_string) #string harus angka
data_float   = float (data_string) #string harus angka
data_bool    = bool (data_string) #false jika string kosong
print ("data =", data_int, ",type = ", type (data_int))
print ("data =", data_float, ",type = ", type (data_float))
print ("data =", data_bool, ",type = ", type (data_bool)) 

