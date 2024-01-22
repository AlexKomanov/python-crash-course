# hashing -> 435245454543623524543
alex_info = {
    "name": "Alex",
    "age": 35,
    "my_languages": {
        "first:": "Java"
    },
    "grades": 80.5,
    # 80: "Karmiel",
    # 105.6: "Coord",
    # ("name", "last_name"): ["Alex", "Komanov"],
    # "name": "Alexander",
}

# print(alex_info["name"])
print(alex_info)
# print(alex_info.keys())
# print(alex_info.values())
# print(alex_info.items())
# print(list(alex_info.items()))
# print(list(alex_info.items())[0])

# print(alex_info.get("grades"))
# print(alex_info["grades"])

# print(alex_info.popitem())
alex_info.update({"has_car": True})
alex_info["father"] = "Victor"
print(alex_info)
alex_info["car"] = alex_info.pop("has_car")
print(alex_info)