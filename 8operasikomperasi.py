# operasi komperasi
# setiap hasil dari opeasi komperasi adalah boolean
# <, >, >=, <=, ==, is, is not


a = 4
b = 2
# lebih besar dari >
print('==== Lebih besar dari > ======')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# lebih kecil dari <
print('==== Lebih kecil dari < ======')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# lebih besar dari atau sama dengan >=
print('==== Lebih besar dari atau sama dengan >= ======')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# lebih kecil dari atau sama dengan <=
print('==== Lebih kecil dari atau sama dengan <= ======')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

#  sama dengan ==
print('====  sama dengan == ======')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

#  tidak sama dengan !=
print('====  sama dengan != ======')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

print('====  objecy identity is ======')

# is membandingkan memory atau objek atau variable yang diberikan nilai
# a = 4 maka a adalah object yang memakan memory
# 4 sama dengan literal dimana dia hanya digunakan sekali dan tidak memakan memory
x = 5
y = 5
# jika nilainya sama maka akan disimpan dalam 1 memory atau id yang sama
print('nilai x = ', x, 'id =', hex(id(x)))
print('nilai y = ', y, 'id =', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

print('====  objecy identity is ======')

# is membandingkan memory atau objek atau variable yang diberikan nilai
# a = 4 maka a adalah object yang memakan memory
# 4 sama dengan literal dimana dia hanya digunakan sekali dan tidak memakan memory
x = 5
y = 5
# jika nilainya sama maka akan disimpan dalam 1 memory atau id yang sama
print('nilai x = ', x, 'id =', hex(id(x)))
print('nilai y = ', y, 'id =', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

x = 5
y = 6
print('nilai x = ', x, 'id =', hex(id(x)))
print('nilai y = ', y, 'id =', hex(id(y)))
hasil = x is y
print('x is y = ', hasil)

print('====  objecy identity is not ======')
x = 5
y = 5
# jika nilainya sama maka akan disimpan dalam 1 memory atau id yang sama
print('nilai x = ', x, 'id =', hex(id(x)))
print('nilai y = ', y, 'id =', hex(id(y)))
hasil = x is not y
print('x is y = ', hasil)

x = 5
y = 6
print('nilai x = ', x, 'id =', hex(id(x)))
print('nilai y = ', y, 'id =', hex(id(y)))
hasil = x is not y
print('x is y = ', hasil)
