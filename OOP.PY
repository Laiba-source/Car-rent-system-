class Car:
    def __init__(self, stock):
        self.stock = stock

    def displaycar(self):
        print("Total number of cars in stock:", self.stock)

    def rentofcar(self, q):
        if q <= 0:
            print("Enter a value greater than zero.")
        elif q > self.stock:
            print("Enter a value less than or equal to the stock.")
        else:
            total_price = q * 100
            self.stock -= q
            print(f"{q} car(s) rented successfully.")
            print("Total price:", total_price)
            print("Cars left after renting:", self.stock)

# Create the object only once
obj = Car(100)

while True:
    uc = int(input('''
1. Display stocks
2. Rent a car
3. Exit
    '''))

    if uc == 1:
        obj.displaycar()
    elif uc == 2:
        n = int(input("Enter the quantity..."))
        obj.rentofcar(n)
    elif uc == 3:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Please select a valid option.")
