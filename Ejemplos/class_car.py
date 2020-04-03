#Clase Car recibe informacion de un vehiculo

class Car():
    """A simple attempt to represent a car"""

    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #Atributo por default

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer reading to the given value.
           Reject the change if it attempts to roll the odometer back.
        """

        if mileage > self.odometer_reading:
            self.odometer_reading = mileage  
        else:
            print("You can't rollback an odometer.")

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


#Creacion de la clase Batery
class Battery():
    """A simple attempt to model a battery for a electric car."""

    def __init__(self,battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + " -kWh battery")
    
    def get_range(self):
        """print a statement about the range this  battery provides"""
        if self.battery_size == 70:
            range_ = 240
        elif self.battery_size == 85:
            range_ = 270

        message = "This car can go approximately " + str(range_)
        message += " miles on a full charge."
        print(message)


#Creacion de la clase ElectricCar que hereda de la clase car
class ElectricCar(Car):
    """Respresent aspect of a car, specific to electric vehicules."""

    def __init__(self,make,model,year):
        """Initialize attributes of the parents class"""
        super().__init__(make,model,year) #Heredando atributos de car
        self.battery = Battery()



#Instanciando objetos de las clases creadas

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())

#Seteando el valor de un atributo desde la instancia
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Modifying an attribute's values throught a method
my_new_car.update_odometer(10)
my_new_car.read_odometer()

#Increment an attribute's values through a method
print("\n")
my_used_car = Car('subaru','impreza','2006')
print(my_used_car.get_descriptive_name())
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#Instanciando objetos de la clase ElectricCar
print("\n")
my_tesla = ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name()) #LLamando a un metodo heredado de la clase Car

#Accesando al atrinuto battery que a su vez es llama al metodo
#de la clase Battery
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()










