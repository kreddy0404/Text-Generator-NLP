# the list "walks" is already defined
print(sum([walks[i]['distance'] for i in range(len(walks))]) // len(walks))