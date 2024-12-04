# Operator Dictionary

data_dict = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung"
}

#Panjang Dictionary
LENDICT = len(data_dict)
print(f"Panjang dictionary: {LENDICT}")

#Mengecek Key Exist atau Tidak
key = "cup"
CHECKKEY = key in data_dict
print(f"Apakah {key} ada di data_dict: {CHECKKEY}")

#Mengakses Value (read) dengan get
print (data_dict["cup"])
print (data_dict.get("cup"))
print (data_dict.get("kis","data tidak ditemukan"))

#Mengupdate Data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep surasep"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"faqih":"faqih si keren"})
print(data_dict)

#Mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)

