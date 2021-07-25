# the following line reads the list from the input, do not modify it, please
old_list = [int(n) for n in input().split()]

binary_list = [0 if n <= 0 else 1 for n in old_list]
print(binary_list)
