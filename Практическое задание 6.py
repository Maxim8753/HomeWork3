def int_func(chart):
    text = input('введите текст маленькими латинскими буквами разделенные пробелом: ')
    return text.title()

words = input('введите текст маленькими латинскими буквами разделенные пробелом: ').split()
for word in words:
    print(int_func(word))
