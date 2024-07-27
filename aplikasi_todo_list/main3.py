from re import L


def intro():
    print("###################################")
    print("###WELCOME TO THE TO-DO-LIST-APP###")
    print("###################################")

    print("-----------------------------------")

def name_input():
    front_name = input('Masukan nama depan anda : ')
    back_name  = input('Masukan nama belakang anda : ')
    return f"{front_name} {back_name}"

def main_menu():
    print("Ketik 1 untuk menambahkan todo, ")
    print("ketik 2 untuk melihat semua todo,")
    print("ketik 3 untuk menghapus todo,")
    print("ketik 4 untuk menghapus semua todo,")
    print("ketik 5 untuk mengakhiri program,")    
    
def get_user_input():
    while True:
        try:
            user_input = int(input("Silahkan masukan angka sesuai diatas : "))
            if user_input in [1,2,3,4]:
                return user_input
            else:
                print("input tidak valid, silahkan input angka sesuai diatas")
        except ValueError:
            print("input tidak valid, silahkan input angka sesuai diatas")

        
def show_username(full_name):
    print(f"Welcome {full_name}")
    
def add_todos(todos):
    while True:
        todo_name = input('Masukan todo anda, ketik exit untuk keluar : ') 
        if todo_name == 'exit':
            return todos
        else:
            todos.append(todo_name)
    
def exit_program(todos):
    exit_ = input('Apakah anda ingin keluar ?, y or n : ') 
    if exit_ == 'y':
        print('exiting program')
        print(f"todos anda adalah {todos}, jumlah todos anda adalah {len(todos)}")
        exit()
    elif exit_ == 'n':
        print('restarting program (WIP)')
    else:
        print('invalid input')

def show_todos(todos):
    if len(todos) > 0:
        print('your todos is : ')
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo}")
    else:
        print("Todo list is empty")
    
def delete_todos(todos):
    while True:
        todo_delete = int(input('masukan todo yang ingin di hapus, ketik 0 untuk batal : ')) - 1
        if todo_delete == -1:
            return todos
        elif todo_delete >= 0 and todo_delete < len(todos):
            todos.pop(todo_delete)
        else:
            print("input tidak valid, silahkan input angka sesuai diatas")
        

def delete_all_todos(todos):
    sure = input("Apakah anda yakin untuk menghapus semua todos? y or n : ")
    if sure == 'y':    
        todos.clear()
        return todos
    else:
        return todos
    

# COBA CARI ttg if name == main, cara menyimpan hasil kodingan kita di sebuah file

intro()
full_name = name_input()
show_username(full_name)
todos = ['todo1', 'todo2', 'todo3']
while True:
    main_menu()
    user_input = get_user_input()
    #print(f"user input anda adalah {user_input}")
    if user_input == 1:
        todos = add_todos(todos) # same varaible overriding
        print("Kembali ke menu utama 😁")
    elif user_input == 2:
        show_todos(todos)
    elif user_input == 3:
        show_todos(todos)
        todos = delete_todos(todos)
        print("Kembali ke menu utama 😁")
    elif user_input == 4:
        todos = delete_all_todos(todos)
    elif user_input == 5:
        exit_program(todos)
    else:
        print("input tidak valid")    
