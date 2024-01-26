# import custom_packages.our_custom_module
# import custom_packages.our_custom_module as ocm
from custom_packages.our_custom_module import add_two_numbers as add_two, User
# custom_packages.our_custom_module.add_two_numbers(5, 10)

# ocm.add_two_numbers(25, 10)

add_two(25, 60)
print(User.username)
user = User(False)
print(user.is_admin)