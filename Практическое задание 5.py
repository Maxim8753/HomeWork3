def sum_num(**kwargs):
    stop = 0
    while True:
        num_list = input('введите "Q" для выхода ').split()
        for num in num_list:
            if num == 'q' or num == 'Q':
                return stop
            else:
                stop += int(num)
        print(f'Сумма чисел - {stop}')
print(sum_num())