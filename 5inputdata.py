# input data


data = input("Masukan data :")
# setiap inputan akan bernilai string

print("data ", data, "bertipe :", type(data))

angka1 = float(input("Masukan angka :"))
angka2 = int(input("Masukan angka :"))

print("data ", angka1, "bertipe :", type(angka1))
print("data ", angka2, "bertipe :", type(angka2))

# data boolean harus dicasting dlu ke tipe data integer
biner = bool(int(input("Masukan angka :")))
print("data ", biner, "bertipe :", type(biner))
