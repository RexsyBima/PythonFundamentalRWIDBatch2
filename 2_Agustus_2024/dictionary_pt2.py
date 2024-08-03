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

# nested dictionary = dictionary didalam ada dictionary
# num = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]
# Machine Learning -> matriks

# .get() []

alamat = ktp['Alamat']['Kecamatan']
print(alamat)
print(ktp.get('Alamat')['Kecamatan'])
print("----------------------------------------------------------------------------------------")


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

# Modifikasi nilai dalam dictionary
# [] -> cara pakainya ttp berbeda
# .update()

ktp['NIK'] = 'ini value baru'
ktp['Nama'] = 'Budi Setiawan'
ktp['isWNI'] = False
new_hobi = 'Main Game'

ktp['Hobi'].append(new_hobi)
print(ktp)
print("----------------------------------------------------------------------------------------")


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

ktp['Alamat']['Desa'] = 'Bandung'
print(ktp)

# CRUD
# Create, Read, Update, Delete
# operasi pemrograman yg dimana kita/harus bisa membuat data, read data, update data, mendelete data
# Create -> membuat dictionary
# Read -> membaca dictionary dan mengakses/membaca data spesifik dalam dictionary
# Update -> mengupdate dictionary
# Mendelete -> 