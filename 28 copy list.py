## teknik duplikat list

a = ["ucup", "otong", "dudung"]
print(f"a = {a}")

b = a

#merubah member dari a

#merubah kedua list
a[1]="michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

#address dari kedua list a dan b
print(f"adress a = {hex(id(a))}")
print(f"adress b = {hex(id(b))}")

#duplicate list dengan copy

print("membuat list c dengan a.copy()")
c = a.copy()

print(f"adress a = {hex(id(a))}")
print(f"adress b = {hex(id(b))}")
print(f"adress c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("ubah data 0")
c[0] = "dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("ubah data 1")
a[1] = "misel"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")