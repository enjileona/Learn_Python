# Copy Dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep surasep",
    "cuy":"ucuy surucuy"
}

friends = teman_teman.copy()

print (f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"] = "ucup si keren"
print (f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

#Pop Dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends: {friends}\n")

#Pop Dictionary (yang terakhir)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends: {friends}\n")

