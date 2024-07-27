""" 
while loop adalah salah satu jenis loop dalam Python yang digunakan untuk menjalankan sebuah blok kode berulang kali selama kondisi yang ditentukan adalah True. Blok kode akan terus dieksekusi selama kondisi loop while adalah True, dan akan berhenti ketika kondisi tersebut menjadi False.
"""
# Dasar sintaks

"""
while condition: -> boolean condition (True or False)
    blokcode
    blokcode
    blokcode
"""

y = 0
y += 1
# SAME THING
y = 0
y = y + 1

x = 0
while True:
    x += 1
    print(x)