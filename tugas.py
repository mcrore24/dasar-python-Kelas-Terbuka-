
print("---n2---")
n = 10**6
seconn2 = (n)**2
menit = seconn2 * 60
jam = menit * 60
hari = jam * 24
bulan = hari * 30
tahun = bulan * 12
abad = tahun * 100

strmenit = str(menit)
mnol = strmenit.count('0')  # hitung nilai 0
msemua = len(strmenit)  # hitung jumlah data
npm = mnol - 1

strjam = str(jam)
jamnol = strjam.count('0')

strhari = str(hari)
harinol = strhari.count('0')
shari = len(strhari)
nhari = shari - harinol


print("Menit  =  60 x ", "10 ^ ", npm)
print('Jam = 60 x ', "10 ^", jamnol)
print('Hari = 24 x ', strhari[0:nhari], '^', harinol)
print('bulan =', bulan)
print('tahun =', tahun)
print('abad =', abad)
