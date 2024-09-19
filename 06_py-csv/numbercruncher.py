import random
from random import choices

dict = {}

with open('occupations.csv', 'r') as file:
    for line in file:
        lst = line.strip().replace('"', '').rsplit(',', 1) # r.split(',', 1) only splits off the FIRST comma from the right
        dict[lst[0]] = lst[1] # occupation : percentage

del dict['Total'] # removing "Total" key-value pair

all_occupations = list(dict.keys())
occupation_weights = []
for weight in dict.values():
    occupation_weights.append(float(weight) / 100)
print(choices(population = all_occupations, weights = occupation_weights))

