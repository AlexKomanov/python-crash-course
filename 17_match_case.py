value = 35

if type(value) is str:
    print("The value is string")
elif type(value) is int or type(value) is float:
    print("The value is number")
elif type(value) is bool:
    print("The value is boolean")
elif type(value) is list:
    print("The value is list")
else:
    print("The value is of unknown type!")

match type(value):
    case __builtins__.str:
        print("The value is string")
    case __builtins__.int | __builtins__.float:
        print("The value is number")
    case __builtins__.bool:
        print("The value is boolean")
    case __builtins__.list:
        print("The value is list")
    case _:
        print("The value is of unknown type!")


