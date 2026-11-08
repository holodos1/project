# phone = {
#     "product": "samsung",
#     "price": 100000}
# phone["price"] = 90000
# print(phone)
# phone["color"] = "черный"
# print(phone)
# del phone["color"]
# print(phone)

# student = {
#     "name": "Давид",
#     "grade": "4",
#     "subject": "математика"
# }
# print(student["name"], student["grade"], student["subject"])
# student["grade"] = 5
# print(student)

# contacts = {
#     "Anna": "123",
#     "Ivan": "456"
#     }
# contacts["Maria"] = "789"
# contacts["Anna"] = "999"
# print(contacts)
# if "Petr" not in contacts:
#     print("не найден")

# global max_point
# max_point = 0
# scores ={
#     "Math": 95,
#     "English": 82,
#     "Code": 100}
# for subject, points in scores.items():
#     print(f"{subject}, {points}")
# for points in scores.values():
#     if max_point < points:
#         max_point = points
# print(max_point)

shop = {"apple": 50, "banana": 30, "cherry": 80}
sale = {}
for fruit, price in shop.items():
    sale[fruit] = price * (80/100)
    print(f"{fruit}: {price}")
print(sale)

