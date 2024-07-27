""" 
f(x) = x + 10
f(10) = 20
"""

""" 
Fungsi dalam Python adalah sebuah blok kode yang dapat dieksekusi berulang kali untuk melakukan tugas tertentu.

Fungsi dapat menerima input (disebut parameter atau argumen), melakukan beberapa operasi berdasarkan input tersebut, dan mengembalikan output (biasanya disebut return value) setelah operasi selesai dieksekusi.

Fungsi biasanya digunakan untuk mengorganisir dan memecah kode menjadi bagian-bagian yang lebih kecil dan lebih mudah dikelola. Ini membuat kode lebih mudah dibaca, dimengerti, dan dipelihara. Selain itu, fungsi memungkinkan untuk menghindari pengulangan kode yang sama di beberapa bagian program.
"""

""" 
f(x) = x + 10
f(10) = 20

f(x,y) = x * y
f(10,2) = 20
"""

def addition(x):
    output = x + 10
    return output 

# None -> empty/kosong
#calling function cara pakainya 
add1 = addition(20)
print(add1)

def greeting():
    return 'hello world'

hw = greeting()
print(hw)

def add(x,y,z):
    x = x
    y = y
    z = z
    return x + y + z

add2 = add(10,20,30)
print(add2)
print(x)