# -*- coding:utf-8 -*-
"""
By：Bruan- 86178
Date: 2021-07-30 
"""


class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" is now sitting! ")

    def roll_over(self):
        print(self.name.title()+" rolled over! ")

my_dog = Dog('aruan', 6)
your_dog = Dog('lucy', 3)
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + ' ' +self.model
        return long_name.title()

my_newcar =Car('audi', 'a4', '2016')
print ("My car's type is " + my_newcar.get_descriptive_name())


class Battary():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+" kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class Electricar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.binerary = Battary()

    def describe_binerary(self):
        print('This car has a '+str(self.binerary.battery_size)+" - khw battery")

my_tesla = Electricar('tesla','model s',2016)
##print(my_tesla.get_descriptive_name())
##my_tesla.describe_binerary()
##print(my_tesla.binerary.battery_size)
my_tesla.binerary.get_range()