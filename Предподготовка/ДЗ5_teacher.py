import random
min_number = 1
max_number = 100
result = None

while result != '=':
    number= random.randint(min_number,max_number)
    print (number)
    result= input(" = > (загаданное число больше вашего)  < ")
    if result == '>':
        min_number=number+1
        print ('min_number ', min_number )
    elif result == '<':
        max_number = number-1
        print('min_number ', max_number)
print ('Победа')
