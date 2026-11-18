#creating class
class Car:
  def move(self): #adding new method
    print("The car drives on the road")

class Boat:
  def move(self):
    print("The boat sails on water.")

class Drone:
  def move(self):
    print("The drone flies in the sky.")

def start_trip(vehicle): #takes a vehicle object and tells it to run its move() method.
  vehicle.move()

# Instantiate one object of each class
car = Car()
boat = Boat()
drone = Drone()

# Call start_trip() for each object
start_trip(car)
start_trip(boat)
start_trip(drone)

