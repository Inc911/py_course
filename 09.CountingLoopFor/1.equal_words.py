print('Задача 1. Я стал новым пиратом!')

# Старому капитану нужно пополнить команду, но на корабль попадут только достойные! Он отобрал десять человек. Те, кто крикнет слово «Карамба», попадут на борт.

# Что нужно сделать

# Пользователь вводит десять слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».
pirates_count = 0
for caramba in range(0, 10):
    caramba = input('Введите слово:\n> ')
    if caramba == "Карамба":
        pirates_count += 1
        print("ArrrCarrramba!!!", pirates_count)
    else:
        print("Geraway!")
print("\nCrew amount", pirates_count)
