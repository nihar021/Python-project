class Bikerent:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print('Total Bikes',self.stock)
    def rentforBike(self,q):
        if q <= 0:
            print("Enter a positive value")
        elif q > self.stock:
            print('Enter the value less than current stock')
        else:
            self.stock=self.stock-q
            print("Total Price",q*100)
            print("Total Bikes",self.stock)


while True:
    obj=Bikerent(100)
    uc=int(input('''
             1.Display stocks
             2.Rent Bike
             3.Exit'''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
         n=int(input("Enter the quantity:--"))
         obj.rentforBike(n)
    else:
        break