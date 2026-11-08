# ttl_amount = float(input("введите сумму покупки в рублях: "))
# if ttl_amount > 1000:
#     discount = 0.10
# else:
#     discount = 0.05
# final_price = ttl_amount * (1 - discount)
# print(f"итоговая сумма к оплате: {final_price:.2f} руб.")

# s1 = float(input("введите сторону a: "))
# s2 = float(input("введите сторону b: "))
# s3 = float(input("введите сторону c: "))
# if s1 > 0 and s2 > 0 and s3 > 0 and (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
#     print("треугольник существует")
# else:
#     print("треугольник не существует")

# balance = 10000
# for i in range(3):
#     withdrawal_amount = int(input(f"итерация {i + 1}/3, введите сумму для снятия: "))
#     if balance >= withdrawal_amount:
#         balance -= withdrawal_amount  
#         print(f"успешно снято: {withdrawal_amount}₽, текущий баланс: {balance}₽")
#     else:
#         print("недостаточно средств")
# print(f"цикл завершен, остаток на балансе: {balance}₽")

# for i in range(7):
#     item = input("что кладем в посылку? ")
#     if item.lower() == "стекло":
#         print("стекло нельзя! пропускаем")
#         continue
#     else: 
#         print(f"{item} добавлен в коробку")
# print("посылка собрана и готова к отправке!")

# n = 5
# for i in range(1,n + 1):
#     a = "" * (n - i)
#     b = "*" * (2 * i - 1)
#     print(a + b)
# for i in range(n - 1, 0, -1):
#     a = "" * (n - i)
#     b = "*" * (2 * i - 1)
#     print(a + b)

# userChoice = None
# while userChoice:
#     def uborka():
#         print("уборка началась")
#     def zaryadka():
#         print("пылесос встал на зарядку")
#     def prokatitKota():
#         print("кот был напуган после такого")
#     pilesos = input("1 - начать уборку, 2 - поставить пылесос на зарядку, 3 - прокатить кота под музыку на пылесосе или напиши стоп чтобы завершить цикл ")
#     if pilesos == "1":
#         uborka()
#     elif pilesos == "2":
#         zaryadka()
#     elif pilesos == "3":
#         prokatitKota()
#     elif pilesos == "стоп":
#         print("дасвидания")
#         break
#     else:
#         print("некорректные данные")

# def calculate_tax(salary):
#     if salary < 50000:
#         return salary * 0.13
#     else:
#         return salary * 0.15
# def get_net_salary(salary):
#     tax = calculate_tax(salary)
#     return salary - tax
# user_input = input("введите размер зарплаты ")
# if user_input.isdigit():
#     salary = float(user_input)
#     tax_amount = calculate_tax(salary)
#     net_salary = get_net_salary(salary)
#     print(f"налог: {tax_amount}, на руки: {net_salary}")
# else:
#     print("некорректные данные")

# total_km = 0
# def log_run(km):
#     global total_km
#     total_km += km
# def show_progress():
#     print(f"всего пройдено: {total_km} км")
# log_run(4)
# show_progress()
# log_run(6)
# show_progress()
# log_run(3)
# show_progress()

# from datetime import datetime
# today = datetime.now().date()
# print(f"месяц: {today.month} день: {today.day} год: {today.year}")

# guests = []
# print("введите имена 5 гостей")
# for i in range(5):
#     name = input(f"введите имя гостя №{i + 1} ")
#     guests.append(name)
# late_guest = input("введите имя гостя который опоздал ")
# if late_guest in guests:
#     guests.remove(late_guest)
#     print(f"гость {late_guest} удален из списка приглашенных")
# else:
#     print(f"гостя с именем {late_guest} не было в списке")
# print("итоговый список приглашенных на вечеринку:")
# print(guests)

# days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
# work_days = days[0:5]
# print("рабочие дни:", work_days)
# days[5] = "выходной!"
# days.reverse()
# print("список в обратном порядке:", days)

# user_profile = {
#     "имя": "Алексей",
#     "возраст": 28,
#     "город": "Новосибирск",
#     "хобби": ["программирование", "чтение", "бег"]
# }
# user_profile["город"] = "Москва"
# user_profile["хобби"].append("фотография")
# print("Имя:", user_profile["имя"])
# print("Возраст:", user_profile["возраст"])
# print("Город:", user_profile["город"])
# print("Хобби:", user_profile["хобби"])

grades = {'Ivan': [4,5,4], 'Anna': [5,5,5],'Petr': [3,4,4]}
for name, scores in grades.items():
    average_score = sum(scores) / len(scores)
    if average_score >= 4.5:
        print(name)

