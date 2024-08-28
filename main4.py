import json

def intro():
    print("###################################")
    print("###WELCOME TO THE TO-DO-LIST-APP###")
    print("###################################")
    print("-----------------------------------")



def main_menu():
    main_menu = ("menambahkan todo", "melihat semua todo", "edit todo","menghapus todo", "menghapus semua todo", "mengakhiri program")
    for i, m in enumerate(main_menu, start=1):
        print(f"{i}. {m}")     
    
def get_user_input():
    while True:
        try:
            user_input = int(input("Silahkan masukan angka sesuai diatas : "))
            if user_input in [1,2,3,4,5,6]:
                return user_input
            else:
                print("input tidak valid, silahkan input angka sesuai diatas")
        except ValueError:
            print("input tidak valid, silahkan input angka sesuai diatas")

        
def show_username(full_name):
    print(f"Welcome {full_name}")
    
def add_todo(todos):
    name = input('Masukan todo anda : ') 
    description = input('Deskripsi todo anda : ')
    isImportant = bool(input(f'Apakah todo {name} penting? 1 or 0 : '))
    notes = []
    while True:
        note = input('Masukan catatan ekstra anda, ketik exit untuk keluar : ')
        if note == 'exit':
            break
        else:
            notes.append(note)
    todo = {"name" : name, "description" : description, "isImportant" : isImportant, "notes" : notes}
    todos.append(todo)
    return todos

    
    
def exit_program(db):
    print('exiting program')
    save_json('db.json', db)
    exit()

def show_todos(todos):
    if len(todos) < 1:
        print("Todo list is empty")
    else:
        print('your todos is : ')
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo['name']} - {todo['description']}")
        user_input = int(input('ketik salah satu angka todo untuk melihat detail : '))
        if user_input > 0 and user_input <= len(todos):
            todo = todos[user_input - 1 ]
            print("--------------------------------")
            for key in todo:
                if isinstance(todo[key], bool):
                    match todo[key]:
                        case True:
                            print(f"{key.upper()} = PENTING")
                        case False:
                            print(f"{key.upper()} = TIDAK PENTING")
                elif isinstance(todo[key], list):
                    print("EXSTRA NOTE(S) = ")
                    for i, note in enumerate(todo[key], start=1):
                        print(f"{i}. {note}")
                else:
                    print(f"{key.upper()} = {todo[key]}")
            print("--------------------------------")
        else:
            raise ValueError('input tidak valid, silahkan input angka sesuai diatas')
    
def show_todos_simpler(todos):
    if len(todos) < 1:
        print("Todo list is empty")
    else:
        print('your todos is : ')
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo['name']} - {todo['description']}")    
    
def delete_todos(todos):
    while True:
        todo_delete = int(input('masukan todo yang ingin di hapus, ketik 0 untuk batal : ')) - 1
        if todo_delete == -1:
            return todos
        elif todo_delete >= 0 and todo_delete < len(todos):
            deleted_todo = todos.pop(todo_delete)
            print(f"todo {deleted_todo['name']} has been deleted")
        else:
            print("input tidak valid, silahkan input angka sesuai diatas")
        

def delete_all_todos(todos, username):
    sure = input("Apakah anda yakin untuk menghapus semua todos? y or n : ")
    if sure == 'y':
        todos.clear()
        print(f"All {username} todos has been deleted")
        return todos
    else:
        return todos
    
def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def save_json(filename, db):
    with open(filename, 'w') as file:
        json.dump(db, file)
        
def login(db):
    username = input('username : ')
    password = input('password : ')
    if username in db and db[username]['password'] == password:
        print(f'login success, welcome {username}')
        return db[username]
    else:
        raise ValueError('login failed, username or password is not correct')

def register(db):
    username = input('username : ')
    password1 = input('password : ')
    password2 = input('confirm password : ')
    if password1 == password2 and username not in db:
        db[username] = {"name" : username, "password" : password1, 'todos' : []}
        save_json('db.json', db)
        exit("Register success")
    else:
        raise Exception('password did not match, or username already in use')

# login, register buat para user -> bisa login
if __name__ == "__main__": # Bilang bahwa skrip utama/flow of codenya itu dimulai dari sini!
    db = read_json('db.json')
    intro()

    login_or_register = input('login or register : ')
    match login_or_register:
        case 'login':
            user = login(db)
        case 'register':
            register(db)
        case _:
            raise ValueError('Invalid Input, please input login or register')
        
    while True:
        main_menu()
        user_input = get_user_input()
        match user_input: # input todo V
            case 1:
                while True:
                    user['todos'] = add_todo(user['todos']) # same varaible overriding
                    exit_ = bool(input('Apakah anda ingin keluar dari menu ini? 1 -> yes or 0 -> no : '))
                    if exit_:
                        save_json('db.json', db)
                        print("Kembali ke menu utama 😁")
                        break
            case 2: # show todo V
                show_todos(user['todos'])
            case 3: # edit todo 
                print("Ini adalah menu edit todo")
                # Print kembali show todo
                show_todos_simpler(user['todos'])
                todo_input = int(input('Pilih angka todo yang ingin di edit : ')) - 1
                if todo_input < 0:
                    raise ValueError('input tidak valid, silahkan input angka sesuai diatas')
                print(user['todos'][todo_input])
                for i, key in enumerate(user['todos'][todo_input], start=1):
                    print(f"{i}. {key}")
                user_input = int(input('Pilih angka sesuai diatas untuk mengedit todo: '))
                match user_input:
                    case 1:
                        user['todos'][todo_input]['name'] = input('enter updated todo name : ')                    
                    case 2:
                        user['todos'][todo_input]['description'] = input('enter todo updated description : ')                    
                    case 3:
                        user['todos'][todo_input]['isImportant'] = bool(int(input('enter new important status, 1 -> Important, 0 -> Not important : ')))                    
                    case 4:
                        print("Extra notes : ")
                        for i, k in enumerate(user['todos'][todo_input]['notes'], start=1):
                            print(f"{i}. {k}")
                        indeks_input = int(input('Pilih angka sesuai diatas untuk mengedit catatan ekstra : ')) - 1
                        if indeks_input < 0:
                            raise ValueError('input tidak valid, silahkan input angka sesuai diatas')
                        #raise ValueError() if indeks_input < 0 else ...
                        user['todos'][todo_input]['notes'][indeks_input] = input("Masukan extra note disini : ")
            case 4: # delete todos v
                show_todos_simpler(user['todos'])
                user['todos'] = delete_todos(user['todos'])
                print("Kembali ke menu utama 😁")
            case 5: # delete all todos v
                todos = delete_all_todos(user['todos'], user['name'])
            case 6: # exit program v
                exit_program(db)
    