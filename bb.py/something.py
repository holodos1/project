# password = input("введите пароль: ")
# if password == "1111":
#     passSlovo = input("введите кодовое слово: ")
#     if passSlovo == "админ":
#         print("доступ к секретным файлам открыт")
#     else:
#         print("неверное кодовое слово")
#         print("у вас обычный доступ")
# else:
#     print("неверный пароль")
#     print("доступ закрыт")

# userWord = None
# while userWord != "стоп":
#     userWord = input("напиши любое слово, и я выведу это слово. напишешь стоп - сам(а) понимаешь что будет. ")
#     print(userWord) 

# number = 0
# summa = 0
# while number <= 100:
#     number += 1
#     summa += number
# print(summa)

# for i in range(10, 0, -1):
#     print(i)
# print("поехали")

# for i in range(15):
#     robotChoise = input("товар целый? 1 - да, 2 - нет ")
    # cOgI = 0                                              # (cOgI - Counter of Good Items)
    # cObI = 0                                              # (cObI - Counter of Bad items)                                                
#     if robotChoise == "1":
#         cOgI += 1
#     elif robotChoise == "2":
#         cObI += 1
# print(cOgI)
# print(cObI)

# while True:
#     userWord = input("введи любое слово и я ввыведу его в консоль или напиши стоп чтобы прекратить цикл ")
#     if userWord == "стоп":
#         print("цикл завершен. хорошего вам дня")
#         break
#     else:
#         print(userWord)

# for i in range(10):
#     if i == 2 or i == 8:
#         continue
#     print(i)

# for i in range(1,11):
#     print(i, end = "")

# import time
# for i in range(10,0,-1):
#     for j in range(10,1,-1):
#         print(f"\r{i}:{j}", end = ' ')
#         time.sleep(0.1)
# print("время вышло")

# for I in range(10):
#     for j in range(10):
#         print("*", end = '')
#     print()

# for I in range(10):
#     for j in range(I):
#         print("*", end = '')
#     print()

# userName = "Гена"
# def sayHello():
#     print("здравствуй", userName)
# sayHello()

# def fireSpell():
#     print("огненная стрела")
# def iceSpell():
#     print("ледяная стрела")
# def healSpell():
#     print("исцеление")
# userSpell = input("1 - огненная стрела, 2 - ледяная стрела, 3 - исцеление ")
# if userSpell == "1":
#     fireSpell()
# elif userSpell == "2":
#     iceSpell()
# elif userSpell == "3":
#     healSpell()
# else:
#     print("некорректные данные")

# def play():
#     print("запускаем песню")
# def nextSong():
#     print("следующая песня")
# def previousSong():
#     print("предыдущая песня")
# userSong = True
# while userSong:
#     userChoice = input("1 - запускаем песню 2 - следующая песня, 3 предыдущая песня, 4 - закончить цикл ")
#     if userChoice == "1":
#         play()
#     elif userChoice == "2":
#         nextSong()
#     elif previousSong == "3":
#         previousSong()
#     elif userChoice == "4":
#         print("дасвидания")
#         break
#     else:
#         print("некорректные данные")

# def menshe1000():
#     print("комиссия 2%")
# def ot1000d05000():
#     print("комиссия 1,5%")
# def bolshe5000():
#     print("комиссия 1%")
# userChoice = int(input("введите сумму для перевода "))
# if userChoice <= 1000:
#     menshe1000()
# elif userChoice >= 1000 and userChoice <= 5000:
#     ot1000d05000()
# elif userChoice >= 5000:
#     bolshe5000()

# def getSquare(a, b):
#     square = a * b
#     return square
# print("площадь прямоугольника", getSquare(5, 7))
# print("площадь пряумоугольника", getSquare(8, 4))
# print("площадь пряумогольника", getSquare(12, 9))

# dollar_course = 86
# def convert(rub):
#     dollars = rub / dollar_course
#     return print(f"dollars:.f")
# print(convert(500))
# print(convert(750))
# print(convert(1000))

# def delivery(suma, distance):
#     if suma > 2000:
#         resultat = str("Доставка бесплатно")
#     elif 0 < distance < 5:
#         resultat = str("За доставку c вас 200 р.")
#     elif 5 <= distance <= 20:
#         resultat = str("За доставку c вас 500 р.")
#     else:
#         print("Некорректные данные")
#     return resultat
# print(delivery(3000, 3))
# print(delivery(1000, 10))
# print(delivery(5000, 5))

# def apply_discount(price, category):
#     if category == "student":
#         print("скидка 15%")
#     elif category == "pensioner":
#         print("скидка 20%")
#     else:
#         print("скидки нет")
#     return price
# print(apply_discount(1000, "student"))
# print(apply_discount(2000, "pensioner"))

# def someFunction():
#     someVariable = 5
# def moreFunction():
#     global someVariable
#     someVariable = 5
#     result = someVariable * 8
#     return result
# print(someVariable)
# print(moreFunction())

# budget = 5000
# def spend(amount):
#     global budget
#     budget -= amount
#     return f"потрачено {amount} рублей, осталось {budget} рублей"
# print(spend(1000))
# print(spend(3000))
# print(spend(999))

# def checkPassword(input_pass):
#     secret = "12345"
#     password = input("введите пароль ")
#     if input_pass == "12345":
#         print("доступ открыт")
#     else:
#         print("отказано")

# wins = 0
# def win_game():
#     global wins
#     wins += 1
# def show_stats():
#     print(wins)
# win_game()
# show_stats()
# win_game()
# show_stats()
# win_game()
# show_stats()

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

# import time
# for i in range(10):
#     print("прошло 2 секунды")
#     time.sleep(2)

# from datetime import datetime, timedelta
# user_days = int(input("через сколько дней событие? "))
# today = datetime.now()
# event_date = today + timedelta(days=user_days)
# print(f"событие состоится: {event_date.strftime('%d.%m.%Y')}")

# import time
# start = time.time()
# for _ in range(50000000):
#     pass
# end = time.time()
# print(f"выполнение заняло {end - start:.4f} секунд")

# names = []
# names = ['Иван', 'Роберт', 'Артем', 'Катя', 'Максим']
# numbers = [1, 2, 7, 3, 7, 4, 7, 5]
# print(names)
# print(names[1])
# print(names[1:3])
# print(numbers[::3])
# for i in range(len(numbers)):
#     if numbers[i] == 7:
#         print(numbers[i])
# if "Артем" in names:
#     print('человек найден')
# names.append("Витя")
# print(names)
# names.remove('Катя')
# print(names)
# names.pop(4)
# print(names)