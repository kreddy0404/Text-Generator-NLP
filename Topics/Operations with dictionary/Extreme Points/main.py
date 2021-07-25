# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
min_value = min(test_dict.values())
max_value = max(test_dict.values())
min_key = ""
max_key = ""

for key in test_dict.keys():
    if test_dict[key] == min_value:
        min_key = key
    if test_dict[key] == max_value:
        max_key = key

print("min:", min_key)
print("max:", max_key)
