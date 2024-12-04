#Latihan perulangan membuat segitiga

sisi = 10
 
# 1. FOR

#dummy variable
count = 1
for i in range (sisi):
    print ("*"*count)
    count += 1

# 2. WHILE
print ("Awal while")
count = 1
while True:
    print ("*"*count)
    count += 1

    if sisi < count:
        break

print ("akhir while")

# 3. Hanya ganjil 
print ("Awal while")
count = 1
while True:
    if count%2:
        print ("*"*count)
        count += 1
    else:
        count  += 1
        continue
    
    if sisi < count:
        break

print ("akhir while")

# 4. segi3

print ("segitiga")
count = 1
spasi = int(sisi/2)

while True:
    if count%2:
        print ("*"*count)
        spasi -= 1
        count += 1
    else:
        count  += 1
        continue
    
    if sisi < count:
        break

print ("segitiga")




