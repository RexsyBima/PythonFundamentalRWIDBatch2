import json

def intro():
    print("###################################")
    print("###WELCOME TO THE TO-DO-LIST-APP###")
    print("###################################")
    print("-----------------------------------")



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
            if user_input in [1,2,3,4,5]:
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
    exit_ = input('Apakah anda ingin keluar ?, y or n : ') 
    if exit_ == 'y':
        print('exiting program')
        save_json('db.json', db)
        exit()
    elif exit_ == 'n':
        print('restarting program (WIP)')
    else:
        print('invalid input')

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
    username =  "User1" #input('username : ')
    password = "password"     #input('password : ')
    if username in db and db[username]['password'] == password:
        print(f'login success, welcome {username}')
        return db[username]
    else:
        raise ValueError('login failed, username or password is not correct')

def register(db):
    username = input('username : ')
    password1 = input('password :')
    password2 = input('confirm password :')
    if password1 == password2 and username not in db:
        print('register success')
        db[username] = {"name" : username, "password" : password1, 'todos' : []}
        save_json('db.json', db)
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
                        print("Kembali ke menu utama 😁")
                        break
            case 2: # show todo V
                show_todos(user['todos'])
            case 3: # delete todo V
                show_todos_simpler(user['todos'])
                user['todos'] = delete_todos(user['todos'])
                print("Kembali ke menu utama 😁")
            case 4: # delete all todo v
                todos = delete_all_todos(user['todos'], user['name'])
            case 5: # exit program v
                exit_program(db)
            case _:
                raise ValueError("input tidak valid")    
            
            # Edit todo