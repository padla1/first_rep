greeting = input('Введите текст:')

letter = input('Введите букву:')
print(f'Количество букв {letter} = ',greeting.count(letter))
for i in range(len(greeting)):
    if greeting[i] == letter:
        print(f'Индекс буквы {letter} -', i)
