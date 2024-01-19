text = "heLLo world and ALEX!"
# text[2] = "E" # TypeError: 'str' object does not support item assignment
# print(text)
# print(text[2])
# print(text[0:7])
# print(text[0:12:2])
# print(text[::-1])
# print(id(text))
# print(id(text.capitalize()))
print(text)
print(text.capitalize())
print(text.title())
print(text.upper())
print(text.lower())

text_from_web = "Name\t\nId\t\nDate"
print(text_from_web)
formatted_text = text_from_web.replace("\t\n", ',')
print(formatted_text)
print(type(formatted_text))
list_from_string = formatted_text.split(",")
print(list_from_string)
print(list_from_string[2])

new_string = " | ".join(list_from_string)
print(new_string)
print(type(new_string))
