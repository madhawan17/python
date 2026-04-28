############################
class Car:
    def __init__ (self, model, company):
        self.model = model
        self.company = company

    def full_name(self):
        return f"{self.company} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, model, company, battery_size):
        super().__init__(model, company)
        battery_size = battery_size

my_tesla = ElectricCar("model 3", "tesla", 75)
print(my_tesla.model)

# my_car = Car("tata", "nexon")
# print(my_car.model)

# MY_car = Car("tesla", "model 3")
# print(MY_car.full_name())

#######################
