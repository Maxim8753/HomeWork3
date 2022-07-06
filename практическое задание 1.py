def separation(arg1, arg2):

    if arg2 == 0:
       print('на ноль делить нельзя ')
    elif arg1 == '' or arg2 == '':
        print('введите число ')
    else:
        arg1, arg2 = int(arg1), int(arg2)
        separation_arg = arg1 / arg2
        print(int(separation_arg))

print(separation(input('Введите число- '),input('Введите число- ')))
