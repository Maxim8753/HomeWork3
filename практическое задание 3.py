def my_func(arg1,arg2,arg3):
    arg_list = [arg1,arg2,arg3]
    return sum(sorted(arg_list)[1:])
print(my_func(2,5,8))