# number = 0
#
# while number <= 10:
#     # if number == 7:
#     #     print(number)
#     #     break
#     print(number)
#     number += 1
# else:
#     print("Else block")
# print("After while loop")

# number = 0
# while number < 5:
#     print(number)
#     number += 1
#
# for num in range(5):
#     print(num)

computer_number = 60
user_number = int(input("Guess a number: "))

while computer_number != user_number:
    if user_number > computer_number:
        print("Please provide a smaller number")
    else:
        print("Please provide a bigger number")

    user_number = int(input("Guess a number: "))
else:
    print("You WIN!")
