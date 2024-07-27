# fungsi intro todo list
print("###################################")
print("###WELCOME TO THE TO-DO-LIST-APP###")
print("###################################")

print("-----------------------------------")
# end

# fungsi ambil input nama
front_name = input('Masukan nama depan anda : ')
back_name  = input('Masukan nama belakang anda : ')
# end

# fungsi menu utama
print("Ketik 1 untuk menambahkan todo, ")
print("ketik 2 untuk melihat semua todo,")
print("ketik 3 untuk menghapus todo,")
print("ketik 4 untuk mengakhiri program,")
# end

# fungsi input menambahkan todo
while True:
    try:
        user_input = int(input("Silahkan masukan angka sesuai diatas : "))
        if user_input in [1,2,3,4]:
            break
        else:
            print("input tidak valid, silahkan input angka sesuai diatas")
    except ValueError:
        print("input tidak valid, silahkan input angka sesuai diatas")
# end

# fungsi pengecekan user input 
if user_input == 1:
    print("ini nambahin todo")
elif user_input == 2:
    print("ini melihat semua todo")
elif user_input == 3:
    print("ini menghapus todo")
elif user_input == 4:
    print("ini mengakhiri program todo")
else:
    print("input tidak valid")
# end

# fungsi showing name 
print(f"Welcome {front_name} {back_name}")
# end


# fungsi masukin todos
todos = []
while True:
    todo_name = input('Masukan todo anda, ketik exit untuk keluar : ') 
    if todo_name == 'exit':
        break
    else:
        todos.append(todo_name)
# end fungsi
   

# fungsi akhiri program (y or n)   
exit_ = input('Apakah anda ingin keluar ?, y or n') 
if exit_ == 'y':
    print('exiting program')
    print(f"todos anda adalah {todos}, jumlah todos anda adalah {len(todos)}")
    exit()
elif exit_ == 'n':
    print('restarting program (WIP)')
else:
    print('invalid input')
# end