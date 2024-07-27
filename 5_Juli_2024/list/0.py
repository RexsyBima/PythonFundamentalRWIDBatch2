# tipe data yg menyimpan serangkaian items dalam urutan tertentu
#             0       1         2
students = ["Joni", "Budi", "Setiawan"] # kumpulan data
#            -3       -2        -1      SUPPORT INDEKS NEGATIF

student1 = students[-1] # indeks python selalu mulai dari 0

print(student1)

# list di python bersifat mutable -> isiannya bisa dirubah2

# menambah element didalam list/ nambah value dalam list, itu kita ada namanya method append()
students = ["Joni", "Budi", "Setiawan"] # kumpulan data
new_student = "Joko"
new_student2 = "Budiman"
students.append(new_student)
students.append(new_student2)
print(students)

# list di python juga bisa gabungkan antara dua list jadi satu, list 1, n 2 = list3. ada method extend()
students = ["Joni", "Budi", "Setiawan"] # kumpulan data
new_students = ["Budiman", "Joko"]
students.extend(new_students)
print(students)

# menghapus elemen didalam list dengan del keyword
students = ["Joni", "Budi", "Setiawan"] # kumpulan data
del students[2]                     # del -> delete
print(students)
# keyword -> mengakses fitur khusus didalam python nanti

# menghapus elemen didalam list dengan method .remove() yang pertama kali ketemu
students = ["Joni", "Budi", "Setiawan", "Budi"] # kumpulan data
students.remove("Budi")
print(students)

# mengahpus elemen didalam list dengan method .pop() # nge cut 
students = ["Joni", "Budi", "Setiawan", "Budi"] # kumpulan data
x = students.pop(-1)
print(students)
print(x)

names = ["Joni", "Budi", "Setiawan", "Budi"] # jumlahnya ada 4
jumlah_names = len(names)
print(jumlah_names)