# def print_hello(name: str):
#     print(f"Hello {name}!")
#
#
# print_hello("Alex")
#
# lambda_print_function = lambda name: print(f"Hello {name}")
# lambda_print_function("Yan")

# def sum_of_numbers(number_1: int, number_2: int):
#     return number_1 + number_2
#
#
# print(sum_of_numbers(5, 10))
#
# lambda_sum_of_nums = lambda num1, num2: num1 + num2
# print(lambda_sum_of_nums(10, 20))

original_list = [10, 20, 30, 40, 50]


# def filtering(elem: int):
#     return elem > 35


filtered_result = list(filter(lambda elem: elem > 5, original_list))
print(filtered_result)
