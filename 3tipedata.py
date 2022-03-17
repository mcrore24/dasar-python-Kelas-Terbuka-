# a = 10 maka a adalah variable yang mempunyai nilai 10

# tipe data angka satuan (integer) yang tidak mempunyai koma

# memanggil library tipe data C
from ctypes import c_double, c_char, c_byte

data_integer = 1
print("data_integer :", data_integer, "beripe data : ", type(data_integer))

# tipe data angaka dengan koma (float)
# tida data doble sama dengan tipe data float jadi tipe data double dimasukan di float
data_float = 10.5
print("data_float :", data_float, "beripe data : ", type(data_float))

# tipe data  dengan kumpulan karakter (string)
data_string = "sabe"
print("data_string :", data_string, "beripe data : ", type(data_string))


# tipe data  dengan nilai 0 , 1 dan atau true atau false (boolean)
data_bol = True
print("data_bol :", data_bol, "beripe data : ", type(data_bol))

# TIPE DATA KHUSUS

# tipe data  komplex
data_complex = complex(5, 6)
print("data_complex :", data_complex, "beripe data : ", type(data_complex))

# karena bahasa python dibuat dari bahasa c maka tipe data c dapat digunakan dengna memanggil library c


# yang berarti memanggi tipe data c_double
data_c_double = c_double(10.5)
print("data_c_double :", data_c_double, "beripe data : ", type(data_c_double))
