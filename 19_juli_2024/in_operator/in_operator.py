# in -> mengecek sebuah value ada didalam tipe data sequence atau bukan (list, tuple, set) + string

numbers = [1,2,3]

if 1 in numbers:
    print('hello world') 

email_str = "reregmail.com" # sebuah email pasti akan ada tanda @

if "@" in email_str:
    print("this is email str")
else:
    print("this is not an email str")