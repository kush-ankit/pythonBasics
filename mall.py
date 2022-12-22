amount = int(input("Enter the shopping amount\n"))

if amount <= 5000:
    Discounted = amount - amount*0.05
    print("Discounted Amount is " + str(Discounted))
    print("Discount is " + str(amount*0.05))
elif amount > 5000 and amount <= 10000:
    Discounted = amount - amount*0.1
    print("Discounted Amount is " + str(Discounted))
    print("Discount is " + str(amount*0.1))
elif amount > 10000 and amount <= 15000:
    Discounted = amount - amount*0.15
    print("Discounted Amount is " + str(Discounted))
    print("Discount is " + str(amount*0.15))
elif amount > 15000 and amount <= 20000:
    Discounted = amount - amount*0.2
    print("Discounted Amount is " + str(Discounted))
    print("Discount is " + str(amount*0.2))
else:
    print("The amount is ",amount)
