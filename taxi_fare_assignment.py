

#the constant
BASE_FARE = 4.00

#function for the taxi fare
def taxi_fare(kilo):
    """
    1. Takes the user input of the kilometers (kilo) of the ride and converts it to meters
    2. Next it computes the equation for the fare of the ride : 4.00 + 0.25(x/140), using the constant BASE_FARE (4.00)
    3. returns the final price of ride to the function 
    """
    meters = kilo*1000
    total_fare = BASE_FARE + (0.25*(meters/140))
    return total_fare
        
#takes user input of how many kilometers was the ride 
kilo = float(input("How many kilometers was the ride? : "))

#prints out the price of the ride to user
#checks if it is divisble by 7 so it could add another 0 to end of it. Else, print with regular two numbers after decimal
if kilo%7==0:
    print(f"${round(taxi_fare(kilo), 2)}0")
else:
    print(f"${round(taxi_fare(kilo), 2)}")


