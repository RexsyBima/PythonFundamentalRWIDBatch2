# for loop sama while loop

"""
For loop adalah jenis loop dalam Python yang digunakan untuk melakukan 
iterasi atau perulangan melalui sebuah sequence seperti list, tuple, string, atau range.
For loop memungkinkan Anda untuk mengeksekusi blok kode tertentu untuk setiap elemen 
dalam sequence tersebut.
"""

numbers = [1,2,3,4]
for n in numbers: # untuk setiap iterasi/item n didalam numbers, eksekusi kode dibawah
    print(f"number is {n}")


names = ['budi', 'bimbim', 'setiawan']    
for i in names:
    print(i)
    
name = 'joni'
for l in name:
    print(l)
    
    
# range Create a sequence of numbers from 0 to before declared number, and print each item in the sequence:
for n in range(1, 4+1):
  print(n)