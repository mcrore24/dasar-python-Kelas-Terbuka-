import time
start_time = time.time()

# setiap baris akan diekseskusi perbaris awal
# baris kosong dan coment tidak akan dieksekusi
print("hello world")
a = 10
print(a)
# sytax python juga dapat di compile dalam bentuk bytecode
# python -m py_compile 1helloword.py(nama file ) code tersebit dijalankan di  terminal
# setelah dijalankan otomatis akan ada folder __pycache__ didalam folder tersebut adalah hasil compile
# setiap perubahan dalam sytax harus di compile ulang
# setiap hasil yang didapat akan

print(time.time() - start_time, "detik")

# compile akan lebih cepat dijalankan dari cara awal
