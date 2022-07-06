#def my_func(x,y):
 #   arg_list = [x**y]
  #  return(arg_list)

#print(my_func(2, 4))

def my_func(x, y):
    if y == 0:
        return 1
    elif y > 0:
        return '"y" должен быть меньше 0 '
    else:
       return my_func(x, y + 1)/x

print(my_func(2, -3))

#def my_func(x,y):
#    return 1 if y == 0 else my_func(x, y + 1)/x

#print(my_func(2,-2))