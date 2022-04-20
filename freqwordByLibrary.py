from collections import Counter

str="hello hello how do do you you you do you"
count=Counter(str.split())
str2=count.most_common(1)
# print(type(str2))
print(str2)