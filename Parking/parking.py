import datetime

"""
Parking Lot
    -Can accomodate up to 5 cars
    -50.00 Flat rate
    -Fee increases per minute
"""

parking_lot = []

class Parking:
    def __init__(self,plateno):
        self.plateno = plateno
        self.time_in = 0
        self.time_out = 0

    def park_car(self):
        if len(parking_lot) > 5:
            print('Parking lot is full')
        else:
            self.time_in = datetime.datetime.now()
            parking_lot.append(self.plateno)
            print(f"Thank you for parking\n{self.plateno}\nOur flat rate is 50.00 \n{self.time_in.strftime('%B %d %Y %I : %M %p')}")


    def leave_parking(self):
        self.time_out = datetime.datetime.now()
        print(f'Exit time:\n{self.time_out.strftime("%B %d %Y %I : %M %p")}')
        self.compute_time()


    def compute_time(self,cash=0):
        consumed_time = ((self.time_out - self.time_in).seconds)/60  #Consumed time in minutes
        total_time = divmod(consumed_time,60)  # returns a tuple of consumed time in hours and minutes [0] hr, [1] min
        print(f"You consumed {total_time[0]} hours, {int(total_time[1])} minute(s)")

        hourly_rate = 100
        # divide minutes by 60 and multiple by 100 compute fee in minutes
        total_bill = round((total_time[0] * hourly_rate) + ((total_time[1]/60)*100),2) + 50

        print(f'Total fee is {total_bill}')
        if cash <= 0:
            try:
                cash = float(input('Enter a bill\n>'))
            except ValueError:
                print('Please enter an amount.')
                return
        print(f'We received {cash}')
        self.compute_bill(cash,total_bill)


    def compute_bill(self,cash,total_bill):
            if total_bill > cash:
                print(f'Not enough cash, total bill is {total_bill}')
                choices = input('Add cash or pay higher bill?\nType "add" to add cash or type "pay" to pay with higher bill\n>').lower()
                if choices == 'add':
                    add_cash = float(input('Enter amount to add\n>'))
                    total_cash = cash + add_cash
                    return self.compute_time(cash=total_cash)
                else:
                    new_cash = float(input('Enter new bill\n>'))
                    return self.compute_time(cash=new_cash)
            change = cash - total_bill
            if change <= 0 :
                print('Thank you for parking!')
            else:
                print(f'Your change is {round(change,2)} Thank you for parking!')
            parking_lot.remove(self.plateno)


    def __str__(self):
        return f'{self.plateno}'
