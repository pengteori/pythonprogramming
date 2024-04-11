def rep_char(length):
    modified_length=length+2
    if length<17:
        print('-'* 19)
    elif length==17:
        print('-'* 19)
    else :
        print('-' * modified_length)

name = input('Input his/her name: ')

length = 7+len(name)

rep_char(length)
print(' Hello ', name, ',', sep='')
print(' Welcome to Seoul.')
rep_char(length)
