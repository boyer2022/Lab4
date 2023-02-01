import random
# setting length of list
length_of_list = 5
list_to_use = []

max_number = 1000
min_number = 2
# Randomly fill list with numbers from 2-1000 with length of list
for i in range(length_of_list):
    random_num = random.randint(min_number, max_number)
    list_to_use.append(random_num)

print(list_to_use)
print(min(list_to_use))

items = [2, 2.4, False, 2.3]

print(min(items))