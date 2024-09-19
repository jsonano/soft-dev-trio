from random import choices

dict = {}

with open('occupations.csv', 'r') as file:
    for line in file:
        lst = line.strip().replace('"', '').rsplit(',', 1) # r.split(',', 1) only splits off the FIRST comma from the right
        dict[lst[0]] = lst[1] # occupation : percentage

del dict['Job Class'] # removing "Job Class" labels
del dict['Total'] # removing "Total" key-value pair

all_occupations = list(dict.keys())
occupation_weights = [float(x) / 100 for x in dict.values()] # converting percentages into decimals | 5.5 --> 0.055
# print(all_occupations)
# print(occupation_weights)
print(choices(all_occupations, weights = occupation_weights)) # random.choices(list, weighted_percentages)
