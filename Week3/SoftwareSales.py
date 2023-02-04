# Calculate the total cost of products. Ask user for total products
# purchased. Calculate discount and return total

# 10-19 = 10%
# 20-49 = 20%
# 50-99 = 30%
# 100 or more = 40%

productCount = input('Enter amount of products you are purchasing ')
productCount = int(productCount)

if(productCount >= 10 and productCount<= 19):
    total = 99-(99*.1)
    print(f'Your total is {total}. You saved {99*.1}')
elif(productCount >= 20 and productCount <= 49):
    total = 99-(99*.2)
    print(f'Your total is {total}. You saved {99*.2}')
elif(productCount >= 50 and productCount <= 99):
    total = 99-(99*.3)
    print(f'Your total is {total}. You saved {99*.3}')
elif(productCount >= 100):
    total = 99-(99*.4)
    print(f'Your total is {total}. You saved {99*.4}')