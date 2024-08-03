todos = ['datapenting1', 'datapenting2', 'datapenting3']

# with open as
# untuk akses mode read mode write, read -> r -> membaca | write -> w -> menulis
# with open('output.txt', 'w') as file: # as = alias
#     file.writelines(todos)
#     
# with open('output2.txt', 'w') as file:
#     for t in todos:
#         file.write(t + '\n\n') # \n = new line
        
with open('output.txt', 'r') as file:
    data = file.readlines()
    
print(data)
# json -> javascript object notation