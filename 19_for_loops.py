
#
# for number in range(1, 20):
#     if number == 15:
#         print(f"I'm number {number} inside 'break' block")
#         break
#     if number % 2 != 0:
#         continue
#     print(number)
#
# print("After for loop")

# for letter in "Hello World!":
#     print(letter, end=" | ")

# names = ["Alex", "Ilay", "David", "Omri"]
# for name in names:
#     print(f"Good evening, {name}!")

names_tuple = ("Alex", "Ilay", "David", "Yan", "Omri")
for name in names_tuple:
    if name == "Yan":
        print("Test was passed as well")
        break
    print(name)
else:
    print("The expected name was not found!")
