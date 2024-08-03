"""
Dalam Python, dictionaries adalah struktur data yang digunakan untuk menyimpan pasangan kunci-nilai (key-value) yang tidak berurutan dan dapat diubah. Dictionaries juga dikenal sebagai "maps", "hashmaps", atau "associative arrays" dalam bahasa pemrograman lainnya.

Setiap elemen dalam dictionary terdiri dari pasangan kunci-nilai (key-value). Kunci (key) harus bersifat unik dan tidak dapat diubah (immutable), seperti string, tuple, atau angka, sedangkan nilai dapat berupa objek apa pun, termasuk list atau dictionary lainnya. Kunci dan nilainya dipisahkan oleh tanda titik dua : dan setiap pasangan kunci-nilai dipisahkan oleh koma.
"""

#         Key                 Value
ex_ktp = {"NamaLengkap" : "Budi Setiawan", "NIK" : 20220001, 'Agama' : 'Islam', 'TempatLahir' : 'Indonesia'}

#print(ex_ktp)

# Kita buat KTP yg lebih lengkap, jangan terintimidasi dengan cara bacanya. akan diajari di point berikut
ktp = {"NIK" : 1234567890,
       "Nama" : "Remote W. Indonesia",
       "TempatLahir" : "Banyumas",
       "TanggalLahir" : "10-02-1999",
       "JenisKelamin" : "Laki-Laki",
       "Alamat" : {"Desa" : "Wisata Tanjung",
                   "RT" : 4,
                   "RW" : 8,
                   "Kecamatan" : "Purwokerto"},
       "Agama" : "Islam",
       "isMenikah" : False,
       "isBekerja" : True,
       "isWNI" : True,
       "isValidforLife" : True,
       "Hobi" : ["Memancing", "Membaca", "Belajar"]
       }

print(ktp) #
print(f"terdapat {len(ktp)} pasangan key:value pair di dictionary ktp")

# Mengakses value dalam dictionary
# Anda dapat mengakses nilai (value) dalam dictionary dengan menggunakan kunci (key) yang terkait dengan nilai tersebut. ada 2 cara untuk mengakses nilai dalam dictionary:
# Menggunakan tanda kurung braket [ ] dan passing nama kunci/key:
# metode .get(key)
print("----------------------------------------------------------------------------------------")
ex_ktp = {"NamaLengkap" : "Budi Setiawan", 
          "NIK" : 20220001, 
          'Agama' : 'Islam', 
          'TempatLahir' : 'Indonesia'}

nama_lengkap = ex_ktp['NamaLengkap']
nik = ex_ktp['NIK']
agama = ex_ktp['Agama']
tempatlahir = ex_ktp['TempatLahir']
print(nama_lengkap) # Budi Setiawan
print(nik) # 20220001
print(agama) # Islam
print(tempatlahir) # Indonesia

nama_lengkap = ex_ktp.get('NamaLengkap')
print(nama_lengkap)
hobi = ex_ktp.get('hobi')
print(hobi)
hobi = ex_ktp['hobi']
print(hobi)