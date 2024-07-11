print("Hello world")

print("ini adalah kalimat")

sentence = "Hello world from variable sentence"
print(sentence)

# string -> sebuah kalimat/kumpulan karakter/kata yg menggambarkan kalimat
front_name = "Joni" # -> superior/ konvensinya pakai petik dua, atau praktek umumnya itu pakai petik (" ")
middle_name = "Budi"
back_name = 'Setiawan' # -> not superior

full_name = front_name + " " + middle_name + " " + back_name # -> tidak efisien, kalau variabel stringnya banyak akan ribet
print(full_name)

# f-string f=formatted string
front_name = "Joni" # 
middle_name = "Budi"
back_name = 'Setiawan' 

full_name = f"{front_name} {middle_name} {back_name}" # -> di beberapa poin kedepan aku akan selalu pakai f-string
print(full_name)

front_name = "Joni" # 
multiplied = front_name * 8 # -> 2 * 8 = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 || 
                            #string * 8 = string + string + string + string + string + string +string + string
#leet code -> gambar segitiga pakai string -> pakai perkalian ini 
""" 
*
**
***
****
"""

print(multiplied)

front_name = "Joki" # 
middle_name = "Budi"
back_name = 'Setiawan' 
umur = 24
introduction = f"Nama depanku adalah {front_name}, umurku {umur} tahun"
introduction2 = "Nama depanku adalah" + " " + front_name + "," + "umurku" + umur + "tahun"
print(introduction)
print(introduction2)