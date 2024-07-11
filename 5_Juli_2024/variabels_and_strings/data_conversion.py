# kita bisa mengubah tipe data dari satu ke ygg lain (selagi memenuhi syarat), contoh -> integer -> string 

x = 10
print(type(x)) # int -> integer
y = "abc"
print(type(y)) # str -> string

# 10 -> "10"
x = str(x)
print(x, type(x))
z = "123"
z = int(z)
print(z, type(z))

v = 54321
v = str(v)
print(v, type(v))

b = "3.51"
b = float(b)
print(b, type(b))
print(b + 1.0 - 15 + 199 //2 % 35)
