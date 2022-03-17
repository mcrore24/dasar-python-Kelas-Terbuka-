# casting tipe data
# merubah tipe data awal menjadi jadi diinginkan

# dataset integer
print("====INTEGER====")
data_integer = 1
print("data :", data_integer, "beripe data : ", type(data_integer))

data_float = float(data_integer)
data_str = str(data_integer)
data_bool = bool(data_integer)  # akan false jika nilai int 0
print("data  :", data_float, "beripe data : ", type(data_float))
print("data  :", data_str, "beripe data : ", type(data_str))
print("data  :", data_bool, "beripe data : ", type(data_bool))

print("====FLOAT====")
# dataset float
data_float = 1.5
print("data :", data_float, "beripe data : ", type(data_float))

data_integer = int(data_float)  # pembulatan kebawah
data_str = str(data_float)
data_bool = bool(data_float)  # akan false jika nilai float 0
print("data  :", data_integer, "beripe data : ", type(data_integer))
print("data  :", data_str, "beripe data : ", type(data_str))
print("data  :", data_bool, "beripe data : ", type(data_bool))


print("====BOOLEAN====")
# dataset boolean
data_bool = True
print("data :", data_bool, "beripe data : ", type(data_bool))
# akan false jika nilai float 0

data_integer = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data  :", data_integer, "beripe data : ", type(data_integer))
print("data  :", data_str, "beripe data : ", type(data_str))
print("data  :", data_float, "beripe data : ", type(data_float))

print("====STRING====")
# dataset float
data_str = "10"  # data string texk tidak dapat dirubah ke integer
# jika data string kosong maka nilai boolean akan menjadi false
print("data :", data_str, "beripe data : ", type(data_str))

data_integer = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)
print("data  :", data_integer, "beripe data : ", type(data_integer))
print("data  :", data_float, "beripe data : ", type(data_float))
print("data  :", data_bool, "beripe data : ", type(data_bool))
