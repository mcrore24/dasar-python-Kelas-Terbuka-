# OPERASI ARITMATIKA


a = 10
b = 3

# operasi penjumlahan +
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi pengurangan -
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi perkalian *
hasil = a * b
print(a, '*', b, '=', hasil)

# operasi pembagian /
hasil = a / b
# hasil pembgian jika ada koma maka otomatis akan langung menjadi float
print(a, '/', b, '=', hasil)

# operasi eksponen ** pangkat
hasil = a ** b
print(a, '**', b, '=', hasil)

# operasi moduls % (sisa pembagian)
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor divisin // (pembulatan kebawah)
hasil = a // b
print(a, '//', b, '=', hasil)

# prooritas operasi operational precedence
# 1 = ()
# 2 = exponen **
# 3 = perkalian dll * / % //
# 4 = pertambahaban dan pengurangan + -
x = 3
y = 2
z = 4

hasil = x + y * z
print(x, '+', y, '*', z, '=', hasil)

hasil = (x + y) * z
print('(', x, '+', y, ') *', z, '=', hasil)
