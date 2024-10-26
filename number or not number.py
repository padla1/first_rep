string = input('введите строку:')


if string.isdigit() :
    print(string.isdigit())
    print(type(int(string)))

else: print(f'{string} is not number ')