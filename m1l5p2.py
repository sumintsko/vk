#mod 1
data_input = input()
before_count = len(data_input)
formated_string = data_input.lower().replace("!", "").replace("@", "").replace("#", "").replace("%", "")
after_count = len(formated_string)
print(before_count - after_count)
print(formated_string)

                        














