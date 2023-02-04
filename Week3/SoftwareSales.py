# Calculate the total cost of products. Ask user for total products
# purchased. Calculate discount and return total

# 10-19 = 10%
# 20-49 = 20%
# 50-99 = 30%
# 100 or more = 40%

productCount = input('Enter amount of products you are purchasing ')
productCount = int(productCount)
subtotal = productCount*99

if(productCount >= 10 and productCount<= 19):
    total = subtotal-(subtotal*.1)
    print(f'Your total is {total}. You saved {subtotal*.1}')
elif(productCount >= 20 and productCount <= 49):
    total = subtotal-(subtotal*.2)
    print(f'Your total is {total}. You saved {subtotal*.2}')
elif(productCount >= 50 and productCount <= subtotal):
    total = subtotal-(subtotal*.3)
    print(f'Your total is {total}. You saved {subtotal*.3}')
elif(productCount >= 100):
    total = subtotal-(subtotal*.4)
    print(f'Your total is {total}. You saved {subtotal*.4}')
else:
    print(f'Your total is {subtotal}')