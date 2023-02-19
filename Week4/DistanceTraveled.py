# Program goal - take in speed and hours from users trip
# Display the distance traveled for each hour 

# Distance = speed x time

# print('Lets calculate how far you have traveled each hour.')

time = int(input('How many hours have you traveled?'))
speed = int(input('How fast were you going in MPH?'))
distance = 0

for x in range(time):
    distance = ((x+1)*speed) + distance
    print(f'By hour {x+1} you traveled {distance} miles')