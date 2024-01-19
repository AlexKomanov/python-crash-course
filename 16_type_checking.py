value = True

if type(value) is str:
    print("The value is string")
elif type(value) is int:
    print("The value is integer")
elif type(value) is bool:
    print("The value is boolean")
elif type(value) is list:
    print("The value is list")
else:
    print("The value is of unknown type!")

if isinstance(value, str):
    print("The value is string")
elif isinstance(value, int):
    print("The value is integer")
elif isinstance(value, bool):
    print("The value is boolean")
elif isinstance(value, list):
    print("The value is list")
else:
    print("The value is of unknown type!")

