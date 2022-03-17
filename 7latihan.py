# latihan konversi satuan temperatur
# program konversi celcius ke satuan lain


print("==== KONVERSI TEMPERATUR =======")

celcius = float(input('Masukan suhu dalam celcius : '))
print('suhu dalam Celcius', celcius, 'celcius')

# konfersi ke reamur
# (4/5)*c
reamur = (4 / 5) * celcius
print('hasil konversi ke reamur =', reamur, 'reamur')

# konversi fahrenheit
fahrenheit = ((9 / 5) * celcius) + 32
print('hasil konversi ke fahrenheit =', fahrenheit, 'fahrenheit')

# konversi kelvin
kelvin = celcius + 273
print('hasil konversi ke kelvin =', kelvin, 'kelvin')


print('=======TUGAS========')
fahrenheit = float(input('Masukkan Suhu dalam Fahrenheit: '))

celcius = ((5/9) * fahrenheit) - 32

kelvin = celcius + 273

print("Suhu dalam Kelvin:", kelvin)


kelvin = float(input('Masukkan suhu dalam kelvin: '))

celcius = kelvin - 273

fahrenheit = ((9/5) * celcius) + 32

print("suhu dalam fahrenheit:", fahrenheit)
