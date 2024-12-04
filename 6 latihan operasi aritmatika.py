# latihan konversi satuan temperature
# program konversi celcius ke satuan lain

print("\n PROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('masukkan suhu dalam celcius:'))
print ("suhu adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print ("suhu dalam reamur adalah", reamur, "Reamur")

# fahrenheit
fahrenheit = (9/5) * celcius
print ("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print ("suhu dalam kelvin adalah", kelvin, "kelvin")

print ("FAHRENHEIT KE KELVIN")
fahrenheit = float (input('masukkan suhu dalam fahrenheit:'))

celcius = (fahrenheit * 5)/9
kelvin = celcius + 273
print ("suhu dalam kelvin adalah", kelvin, "Kelvin")

print ("KELVIN KE FAHRENHEIT")
kelvin = float (input('masukkan suhu dalam kelvin:'))

celcius = (kelvin-273)
fahrenheit = (9/5) * celcius
print ("suhu dalam kelvin adalah", fahrenheit, "Kelvin")