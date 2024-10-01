from random import choices

occupations_lst = []

with open('occupations.csv', 'r') as file:
    for line in file:
        lst = line.strip().replace('"', '').rsplit(',', 1) # r.split(',', 1) only splits off the FIRST comma from the right
        occupations_lst.append(lst)

print(occupations_lst)
