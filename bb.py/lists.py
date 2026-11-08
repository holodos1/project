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

# fruits = ["яблоко", "груша", "слива"]
# for i, item in enumerate(fruits):
#     print(f"{i}: {item}")

# total_sum = 0
# numbers = [4, 7, 9, 13, 65]
# for i in numbers:
#     print(i * 2)
#     total_sum += i * 2
# print(total_sum)

temps = [12, 15, 18, 14, 20, 22, 19]
temps_sum = sum(temps)
middle_temps = temps_sum / len(temps)
print(min(temps))
print(max(temps))
print(middle_temps)