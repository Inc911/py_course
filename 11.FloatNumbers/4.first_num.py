print('Задача 4. Первая цифра')

# Дано положительное действительное число X. 
# Выведите его первую цифру после десятичной точки. 
# При решении этой задачи нельзя пользоваться условной инструкцией, циклом или строками


while True:
    num = float(input("Please, enter the number:\n>"))
    round_num = int(num * 10)

    print(round_num % 10)

# В 4-ом задании, по условию, необходимо, чтобы программа выводила первую цифру после запятой, например при вводе числа 123.456 , должна выводиться цифра 4, в вашем варианте выводится 5, это задание решить проще, без использования библиотеки math, попробуйте сначала умножить число на 10, преобразовать в целое, а потом получить последнею цифру числа.
