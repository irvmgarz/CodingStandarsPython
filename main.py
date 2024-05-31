class Destination:
    def __init__(self):
        self.my_destinations = {'Paris': 500, 'NYC': 600}
    
    def get_extracost(self, destination):
        return self.my_destinations.get(destination, 0)
    
    def valid_this(self, destination):
        return isinstance(destination,str)

class Passenger:
    def __init__(self, num_people):
        self.num_people = num_people
    
    def valid_num_people(self):
        print("this working here")
        return isinstance(self.num_people,int) and 0 < self.num_people <81

    def get_discount(self):
        if 4 <= self.num_people < 10:
            return 0.1
        elif self.num_people <= 10:
            return 0.2
        else:
            return 0.0
  
class TotalStay:
    def __init__(self, duration):
        self.duration = duration

    def is_valid_total_stay(self):
        return isinstance(self.duration, int) and self.duration > 0

    def get_fee(self):
        return 200 if self.duration < 7 else 0

    def get_the_best_promo_ever(self,num_people):
        return 200 if self.duration > 30 or num_people ==2 else 0 
    
    def get_weekend(self):
        return 100 if self.duration > 7 else 0

class Vacation:
    base_cost = 1000

    def __init__(self, destination, num_people, duration):
        self.destination_name = destination
        self.passenger = Passenger(num_people)
        self.total_stay = TotalStay(duration)
        self.destination = Destination()

    def sum(self):
        # Verifica si las entradas son válidas
        if not self.destination.valid_this(self.destination_name) or not self.passenger.valid_num_people() or not self.total_stay.is_valid_total_stay():
            return -1
        
        # Suma el costo total
        total_cost = self.base_cost
        total_cost += self.destination.get_extracost(self.destination_name)
        total_cost += self.total_stay.get_fee()
        total_cost -= self.total_stay.get_the_best_promo_ever(self.passenger.num_people)

        discount = self.passenger.get_discount()
        total_cost = total_cost - (total_cost * discount)
        
        return max(int(total_cost), 0)

#this is main function
def main():
    #this are the inputs
    destination = "Paris"
    num_people = 5
    duration = 10

    #this are the outputs
    calculator = Vacation(destination, num_people, duration)
    cost = calculator.sum()

    #this will do some printing
    if cost == -1:
        print("Invalid input.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")

#main event function
if __name__ == "__main__":
    main()
