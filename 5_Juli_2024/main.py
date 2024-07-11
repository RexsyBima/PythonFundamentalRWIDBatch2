
import json


def load_todos():
    try:
        with open("todos.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {"todos" : []}


def save_json(todos):
    datas = {"todos" : todos} # kita buat strukturnya menjadi dictionary dengan key todos dan values list of todos
    with open("todos.json", "w") as file:
        json.dump(datas, file)

#kita rubah fitur add banyak todos menjadi fungsi
def insert_todos(todos : list):
    while True:
        todo = input("input your todo here, press 0 to quit inputting the todo : ")
        if todo == "0":
            break
        todos.append(todo)
    return todos

def modify_todos(todos : list):
    while True:
        try:
            todo_index = int(input("insert what number of the todos you want to modify, 0 to break"))
            print(f"nilai todo_index adalah {todo_index}") # untuk testing
            if todo_index == 0:
                break
            elif todo_index > 0:
                todos[todo_index-1] = input("what is the todo you want to put in here?")
            else:
                print("Invalid input, please input value greater than 0")
        except ValueError:
            print("please insert integer value and greater than or equal to 0")
    return todos

def show_todos(todos:list):
    if len(todos) > 0:
         for i,t in enumerate(todos, start=1):
             print(f"{i}. {t}")
    else:
        print("Todo list is empty")



def delete_todo(todos:list):
    while True:
        todo_index = int(input("insert what number of the todos you want to delete"))
        if todo_index == 0:
            break
        todos.pop(todo_index - 1) #indexing starts from zero...
    return todos

def clear_todos(todos : list):
    sure = input("are you sure you want to clear all the todos? type 'yes' to execute, else to no")
    if sure == "yes":
        todos.clear()
        print("clearing todos")
        return todos
    else:
        print("exiting menu")
        return todos

if __name__ == "__main__":
    todos = load_todos()
    #print(todos) # untuk debug, notice nilai keluarnya adalah dictionary dengan key todos dan value list of todos, kita bisa ambil saja todos nya demi kemudahan
    todos = todos["todos"]  #kita access key "todos" untuk mengeluarkan value list "todos"
    print("Welcome to the Todo list app")
    print("your todos : ")
    show_todos(todos)
    while True:
        access_feature = input("press 1 to add todo(s), 2 to modify todos, 3 to show todos, 4 to delete todos, 5 to save todos")
        match access_feature:
            case "1":
                todos = insert_todos(todos)
            case "2":
                todos = modify_todos(todos)
            case "3":
                show_todos(todos)
            case "4":
                todos = delete_todo(todos)
            case "5":
                save_json(todos)
            case "6":
                todos = clear_todos(todos)
            case "7":
                save_json(todos)
                break
            case _:
                print("invalid input, try again.")