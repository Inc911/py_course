print('Задача 1. Конвертация')


# При покупках за рубежом 
# с помощью карты банки делают конвертацию через промежуточную валюту.

# Например, 
# если купить что-то в евро, 
# то сначала эта сумма конвертируется в доллары, а уже потом - в рубли.
# 
# Напишите программу, 
# которая получает на вход стоимость покупки в евро,
# затем выводит ответ в рублях.
# 
# Мы живём в альтернативной реальности,
# где 1 евро = 1.25 доллара, а 1 доллар = 60.87 рублей.
while True:
  eur = int(input("Please, enter the price in euro:\n>"))
  usd = eur / 1.25
  rur = usd * 60.87
  print("Coast in RUR is", round (rur, 2), "rub")