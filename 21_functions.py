import random


#########  Simple function without param

# def print_hello_world():
#     print("Hello, World!!!")
#
#
# print_hello_world()
# print_hello_world()

#########  Function with param
#
# def print_greeting(name: str):
#     print(f"Hello, {name.upper()}")
#
#
# print_greeting("Alex")
# print_greeting("Yan")
# # print_greeting(123) # AttributeError: 'int' object has no attribute 'upper'

#########  Function with params and with return

# def sum_two_numbers(number_1: int, number_2: int):
#     return number_1 + number_2
#
#
# def increase_and_print_result(result: int):
#     print(f"Increased Result is = {result + 1}")
#
#
# regular_result = sum_two_numbers(15, 10)
# print("--->", regular_result)
#
# increase_and_print_result(regular_result)

#########  Function only with return

# def generate_random_number():
#     return random.randint(0, 1000000)
#
#
# print(generate_random_number())

#########  Function with default params and changing order

# def print_worker_bonus(name: str, bonus: int = 3000):
#     print(f"Worker {name.upper()} is going to get bonus of {bonus}!")
#
#
# print_worker_bonus("Alex", 2000)
# print_worker_bonus("Yan")
# print_worker_bonus("Omri", 5000)
# print_worker_bonus(bonus=10000, name="David")


#########  Function with *args
# names = ["Alex", "Yan", "Omri"]
#
#
# def print_list_of_names(list_of_names: list):
#     print(type(list_of_names))
#     print(list_of_names)
#     list_of_names[-1] = "OMRI"
#     print(list_of_names)
#
#
# print_list_of_names(names)
#
#
# def print_tuple_of_names(*list_of_names: str):
#     print(type(list_of_names))
#     print(list_of_names)
#     list_of_names[-1] = "OMRI"
#
#
# print_tuple_of_names("Alex", "Yan", "Omri", "David")


#########  Function with **kwargs

def print_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs.items())


print_kwargs(name="Alex", age=35, is_working=True)
