# user input digunakan untuk meminta user memasukan input (input ketikan di terminal)
# kedalam program kita, input yang dimasukan oleh user akan selalu berbentuk string
# (tetapi tetap bisa dikonversi menjadi tipe data lain, selagi memenuhi syarat konversi tipedata itu)

hobi = input('what is your hobi?')
print(f'your hobi is {hobi}')
print(type(hobi))

age = input('how old are you? ')
age = int(age) #overwrite/override 
print(age, type(age))