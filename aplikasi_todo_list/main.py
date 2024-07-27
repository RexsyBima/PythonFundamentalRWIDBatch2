print("###################################")
print("###WELCOME TO THE TO-DO-LIST-APP###")
print("###################################")

print("-----------------------------------")


front_name = input('Masukan nama depan anda : ')
back_name  = input('Masukan nama belakang anda : ')

# list

print(f"Welcome {front_name} {back_name}")

# mtk = (5 * (10+(5-3)))

jumlah_todos = int(input('Masukan jumlah todos yang anda inginkan : '))
print(type(jumlah_todos))

todos = []
for i in range(1, jumlah_todos + 1):
    todo = input('Masukan todo anda : ') # makan
    todos.append(todo)



if len(todos) == 4:
    print(f"todos anda adalah {todos}, jumlah todos anda adalah {len(todos)}")
elif len(todos) == 2:
    print(f"todos anda adalah {todos}, jumlah todos anda adalah dua")

   
   
exit_ = input('Apakah anda ingin keluar ?, y or n') 
if exit_ == 'y':
    print('exiting program')
    exit()
elif exit_ == 'n':
    print('restarting program (WIP)')
else:
    print('invalid input')
