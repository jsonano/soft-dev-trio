# Jason Chao
# The Flying Mice
# SoftDev
# K05 - Processing Bitstreams
# 2024 - 9 - 17
# Time spent:
import random as r

dict = {}

file = open("krewes.txt", "r")
lst = file.read().split('@@@') # separating each devo using separator '@@@'
lst = lst[0:len(lst) - 1] # removing "\n" from the end

for profile in lst:
    profile_list = profile.split('$$$')  # separating devo info into a list | [pd, devo, ducky]
    dict[profile_list[1]] = profile_list # assigning devo name to their info in dict | devo : [pd, devo, ducky]

devo = r.choice(list(dict.keys()))
devo_info = dict[devo]
print(devo_info)
print(f'Period: {devo_info[0]} \nName: {devo_info[1]} \nDucky: {devo_info[2]}\n')
