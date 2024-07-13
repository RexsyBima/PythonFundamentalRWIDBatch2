# aplikasi pembuatan SIM
# nanti aplikasinya akan ngeprint user berhak membuat sim
# jika usernya umurnya lebih dari 18
# bug -> kesalahan logika didalam kodingan kita
# else selalu ditaruh terakhir
# kode ini tentangg pembuatan sim sederhana

umur = -1 #Tahun
tinggi_badan = 160 #CM

# Operator and: Mengembalikan True jika kedua kondisi/lebih yang diperiksa adalah True.
if 100 > umur > 18 and tinggi_badan >= 175:
    print('user berhak masuk akademi militer')
elif 100 > umur > 18 and tinggi_badan <= 175:
    print('user tidak berhak masuk akademi militer, umur dibawah 18, dan tb kurang dari samadengan 175')
else: #kalau tidak terpenuhi -> jika kondisi if diatas tidak terpenuhi, maka else statement menjadi perintah terakhir
    print('input tidak valid')




#elif 0 < umur <= 18: # else if, kondisional bawahan if yg nanti hanya akan tereksekusi jika kondisi if atau elif sebelumnya tidak terpenuhi
#    print('user tidak berhak masuk akademi militer, umur dibawah 18')
#elif umur > 100:
#    print('input tidak valid, umur terlalu tua untuk masuk akademi militer')
#else: #kalau tidak terpenuhi -> jika kondisi if diatas tidak terpenuhi, maka else statement menjadi perintah terakhir
#    print('input tidak valid')