# / not / or / and

# not

# print(f"not True -> {not True}")
# print(f"not False -> {not False}")
# print(not (5 == 5))

# or
# print(f"True or True -> {True or True}")
# print(f"True or False -> {True or False}")
# print(f"False or True -> {False or True}")
# print(f"False or False -> {False or False}")
# print(f"True or (False or False) -> {True or (False or False)}")

# number_1 = 6
# number_2 = 11
#
# if number_1 == 5 or number_2 == 10:
#     print("At least one number is as expected")
# else:
#     print("No one as expected")

# and

# print(f"True and True -> {True and True}")
# print(f"True and False -> {True and False}")
# print(f"False and True -> {False and True}")
# print(f"False and False -> {False and False}")
# print(f"True or (False and False) -> {True or (False and False)}")

# number_1 = 6
# number_2 = 10
#
# if number_1 == 5 and number_2 == 10:
#     print("All numbers are as expected")
# else:
#     print("Not as expected")

# number = int(input("Please enter a number: "))
#
# if number >= 0 and number <= 20:
#     print("Range of 0 - 20")
# elif number > 20 and number <= 50:
#     print("Range 21 - 50")
# elif 50 < number <= 100:
#     print("Range 51 - 100")
# else:
#     print("No valid number was entered...")

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

correct_username = "Alex"
correct_password = "qwerty123456"

if input_username == correct_username and input_password == correct_password:
    print(f"Welcome '{correct_username}' to the system!")
else:
    print("At least one of the credentials was wrong. Please try again.")
