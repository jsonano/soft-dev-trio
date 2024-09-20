# The Winners - Jason Chao & Colyi Chen
# SoftDev
# K06 -- Reading & Parsing CSV file
# 2024-09-19
# Time spent: 1 hour
'''
DISCO:
- .strip() to remove leading/trailing whitespaces ("\n") from strings
- .replace() to remove unwanted characters from strings
- .rsplit() to split a string from the right
- del dict['key'] to remove a key-value pair from a dictionary
- random.choices(list, weights = weighted_percentages) to randomly select an element from a list based on weighted percentages

QCC:
- Is there another way to remove the "Job Class" and "Total"?
- Is there a way to return the occupations based on percentages without using random.choices()?

INFO:
Comments are added to the code to explain the purpose of each line of code.
'''

from random import choices

occupations_dict = {}

with open('occupations.csv', 'r') as file:
    for line in file:
        lst = line.strip().replace('"', '').rsplit(',', 1) # r.split(',', 1) only splits off the FIRST comma from the right
        occupations_dict[lst[0]] = lst[1] # occupation : percentage

del occupations_dict['Job Class'] # removing "Job Class" labels
del occupations_dict['Total'] # removing "Total" key-value pair

def random_selection(dict):
    all_occupations = list(dict.keys())
    occupation_weights = [float(x) / 100 for x in dict.values()] # converting percentages into decimals | 5.5 --> 0.055
    # print(all_occupations)
    # print(occupation_weights)
    string = str(choices(all_occupations, weights = occupation_weights)) # random.choices(list, weighted_percentages)
    return string[2 : len(string) - 2]

print(random_selection(occupations_dict))
