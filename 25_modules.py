# import custom_module
import custom_module as cm

from custom_module import add_two_numbers, User as U

# custom_module.add_two_numbers(5, 10)
# print(custom_module.basic_url)
# print(custom_module.User.username)
# user = custom_module.User(True)
# print(user.is_admin)

# cm.add_two_numbers(5, 10)
# print(cm.basic_url)
# print(cm.User.username)
# user = cm.User(True)
# print(user.is_admin)

add_two_numbers(20, 15)

user = U(False)
print(U.username)
print(user.is_admin)
