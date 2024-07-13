nama = input('Masukan nama anda : ') #
umur = input('Masukan umur anda : ') #Tahun
umur = int(umur)
tinggi_badan = input('Masukan tinggi badan anda : ') #CM
tinggi_badan = int(tinggi_badan)


# Operator and: Mengembalikan True jika kedua kondisi/lebih yang diperiksa adalah True.
if 100 > umur > 18 and tinggi_badan >= 175:
    print(f'{nama} berhak masuk akademi militer')
elif 100 > umur > 18 and tinggi_badan <= 175:
    print(f'{nama} tidak berhak masuk akademi militer, umur dibawah 18, dan tb kurang dari samadengan 175')
else: #kalau tidak terpenuhi -> jika kondisi if diatas tidak terpenuhi, maka else statement menjadi perintah terakhir
    print('input tidak valid')