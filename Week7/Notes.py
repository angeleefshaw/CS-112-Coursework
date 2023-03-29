# # List in python can be heterogeneous (contains many types)
# # Lists are sequences. 

# # Built in list function
# nums = list(range(104,112))
# print(nums)

# # Determine number of elements in a list
# print(len(nums))

# # Get last element in list
# print(len(nums) - 1)

# # Find the type using built in type function
# print(type(nums[3]))

# # Negative indexing
# print(nums[-1]) #gives the last item in the list

# # List index out of range error: accessing item in list that does't exist

# # Iterate with indexes
# for i in range(len(nums)):
#     print(nums[i])

# # Slicing in python - always returns another list
# print(nums[0:4])
# print(nums[:8]) #shorthand for [0:8]
# print(nums[8:]) #shorthand for [8:]

word = list('Lumberjack')

# print(word)

# print(word['m':'n'])

for total_minutes in range (55, 65):
    hours = total_minutes//60
    minutes = total_minutes%60
    if(minutes < 10): 
        print(str(hours), ":0"+str(minutes))
    else:
        print(str(hours) , ":"+str(minutes))