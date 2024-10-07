# Jason Chao
# The Fire Marshals | Ivan, Tanzeem, and Jason
# SoftDev
# K12 - Combinations
# 2024 - 10 - 01
# Time spent: 1.5 hours

from flask import Flask, render_template
from random import choices

app = Flask(__name__)

occupations_lst = []

with open('data/occupations.csv', 'r') as file:
    for line in file:
        lst = line.strip().replace('"', '').rsplit(',', 2)
        occupations_lst.append(lst)
        
all_occupations = occupations_lst[1 : len(occupations_lst) - 1]
occupation_weights = [float(row[1]) / 100 for row in occupations_lst[1 : len(occupations_lst) - 1]]
# print(all_occupations)
# print(occupation_weights)
# print(occupations_lst)
# choice = choices(all_occupations, weights = occupation_weights)
# random_occupation = choice[0][0]
# random_percentage = choice[0][1]
# string = f'Randomly Occupation: {random_occupation} | Percentage: {random_percentage}'

@app.route("/wdywtbwygp")
def home():
    choice = choices(all_occupations, weights = occupation_weights)
    random_occupation = choice[0][0]
    random_percentage = choice[0][1]
    string = f'Randomly Occupation: {random_occupation} | Percentage: {random_percentage}'
    return render_template("tablified.html", 
                           title = 'Tablified Occupations',
                           heading = 'Choosing Random Occupations with a Table',
                           team_info = 'The Fire Marshals | Ivan, Tanzeem, and Jason',
                           random_selection = string,
                           occupations = occupations_lst,
                           )

if __name__ == "__main__":
    app.debug = True
    app.run()
