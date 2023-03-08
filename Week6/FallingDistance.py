# Write a program that calculates the distance an object falls in a time period

# The formula to calculate distance d=12gt2

g = 9.8

timeRange = 10
def fallingDistance (time): 
    return (12*9.8*time*2)

# Write a program that calls the fallingDistance function
# in a loop for a timeRangg of 10. Display their distance
for i in range(timeRange):
    print(round(fallingDistance(i), 2))