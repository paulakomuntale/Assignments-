from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("car is starting")

    @abstractmethod
    def stop(self):
        print("car is stopping")

class Car(Vehicle):
    def __init__(self):
        pass

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

car = Car()
car.start()
car.stop()
