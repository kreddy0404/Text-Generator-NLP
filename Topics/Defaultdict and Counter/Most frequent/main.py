from collections import Counter

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")
text_list = text.split()

count_dict = Counter(text_list)
for t in count_dict.most_common(int(input())):
    print(*t)