# Jason Chao
# The Flying Mice
# SoftDev
# K05 - Processing Bitstreams
# 2024 - 9 - 17
# Time spent:

dict = {}

file = open("krewes.txt", "r")
lst = file.read().split('@@@')
lst = lst[0:len(lst) - 1]

for profile in lst:
    profileList = profile.split('$$$')
    dict[profileList[1]] = profileList

