"""
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.


Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
"""
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        
           
class Bus(Vehicle):
    def __init__(self,seat_capacity,max_speed,mileage):
        super().__init__(max_speed,mileage)        
        self.seat_capacity=seat_capacity
        
    def default(self):
        total_fare=self.seat_capacity * 100
        fare=total_fare*.10
        final_price= fare + total_fare
        return final_price
    
bus=Bus(20,10,50)
print(f"Bus fare: {bus.default()}") 