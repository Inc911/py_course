print('Задача 4. Марсоход 2\n')

# К роботу Валли отправили «коллегу» Билли. Это его первая высадка на Марс, поэтому его тестируют в прямоугольном помещении размером 15 × 20 м. Марсоход высаживается в центре комнаты (в точке 8, 10), затем управление им передаётся оператору, то есть пользователю вашей программы.

# Программа спрашивает, в какую сторону оператор хочет направить робота: север (клавиша W), юг (клавиша S), запад (клавиша A) или восток (клавиша D). Оператор делает выбор, марсоход перемещается в эту сторону на один метр, а программа сообщает новую позицию робота. Если марсоход упёрся в стену, он не должен пытаться переместиться в сторону стены — в этом случае его позиция не меняется.

# Что нужно сделать
# Создайте программу для управления роботом Билли.

# Пример:
#
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
room_length = 20
room_width = 15
x = 18
y = 13

while True:
    print("Mars rover is on", x, y, "point.\n")
    direction = input("Please choose the direction (W/S/A/D) \n>")
    if x <= room_length and x >= 0 and y <= room_width and y >= 0:
        if direction == "W":
            y += 1
        elif direction == "S":
            y -= 1
        elif direction == "A":
            x -= 1
        elif direction == "D":
            x += 1

        else:
            print("Please, enter correct direction!!")

    if x > room_length:
        print("\nYou're stumped!\nPlease change the direction!")
        x -= 1
    if x < 0:
        print("\nYou're stumped!\nPlease change the direction!")
        x += 1
    if y > room_width:
        print("\nYou're stumped!\nPlease change the direction!")
        y -= 1
    if y < 0:
        print("\nYou're stumped!\nPlease change the direction!")
        y += 1

# |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
# -------------------------------
# |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
# |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
# |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
# |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
# |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
# |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
