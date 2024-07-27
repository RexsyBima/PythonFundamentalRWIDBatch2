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
    print("ketik 4 untuk mengakhiri program,")    
    
def get_user_input():
    while True:
        try:
            user_input = int(input("Silahkan masukan angka sesuai diatas : "))
            if user_input in [1,2,3,4]:
                break
            else:
                print("input tidak valid, silahkan input angka sesuai diatas")
        except ValueError:
            print("input tidak valid, silahkan input angka sesuai diatas")

def user_input_check():
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
        
def show_username(full_name):
    print(f"Welcome {full_name}")
    
def add_todos():
    todos = []
    while True:
        todo_name = input('Masukan todo anda, ketik exit untuk keluar : ') 
        if todo_name == 'exit':
            break
        else:
            todos.append(todo_name)
    
def exit_program():
    exit_ = input('Apakah anda ingin keluar ?, y or n') 
    if exit_ == 'y':
        print('exiting program')
        print(f"todos anda adalah {todos}, jumlah todos anda adalah {len(todos)}")
        exit()
    elif exit_ == 'n':
        print('restarting program (WIP)')
    else:
        print('invalid input')


intro()
full_name = name_input()
show_username(full_name)

"""  
show_username(name_input()) #readabilitynya kurangg
"""