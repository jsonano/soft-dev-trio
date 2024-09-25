# Jason Chao, Ivan Gontchar, Tahmim Hassan
# The Fire Wizards
# SoftDev
# K09 -- Flask
# 2024 - 9 - 24
# Time spent: 1 hour

from flask import Flask
app = Flask(__name__)

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

@app.route("/")
def output1():
    print(__name__)
    string = ""
    for occupation in occupations_dict:
        string += occupation + "<br>"
    return f'<strong>ALL OCCUPATIONS</strong><br> {string} <br><strong>Selected Occupation | {random_selection(occupations_dict)}</strong>'

# def output2():
#     return random_selection(occupations_dict)
    
app.run()