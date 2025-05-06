class Ride:
    def __init__(self, distance, base_fare=5.0):
        self._distance = distance  # Private attribute
        self._base_fare = base_fare  # Private attribute

    @property
    def distance(self):
        return self._distance

    @property
    def base_fare(self):
        return self._base_fare

    def calculate_fare(self):
        """Abstract method to be implemented in subclasses"""
        raise NotImplementedError("Subclasses must implement this method")
    
class CarRide(Ride):
    def calculate_fare(self):
        """Calculates fare for a car ride"""
        return self.base_fare + (self.distance * 1.5)

class BikeRide(Ride):
    def calculate_fare(self):
        """Calculates fare for a bike ride"""
        return self.base_fare + (self.distance * 0.8)

class TruckRide(Ride):
    def calculate_fare(self):
        """Calculates fare for a truck ride"""
        return self.base_fare + (self.distance * 2.0)
    
class RideLogger:
    @staticmethod
    def log_ride(ride_type, distance, fare):
        print(f"Ride Type: {ride_type}, Distance: {distance} miles, Fare: ${fare:.2f}")

def process_ride(ride):
    fare = ride.calculate_fare()
    RideLogger.log_ride(type(ride).__name__, ride.distance, fare)
    return fare

# Example Usage
car_ride = CarRide(10)  # 10 miles
bike_ride = BikeRide(5)  # 5 miles
truck_ride = TruckRide(15)  # 15 miles

# Processing rides
process_ride(car_ride)   # Output: Ride Type: CarRide, Distance: 10 miles, Fare: $20.00
process_ride(bike_ride)  # Output: Ride Type: BikeRide, Distance: 5 miles, Fare: $9.00
process_ride(truck_ride) # Output: Ride Type: TruckRide, Distance: 15 miles, Fare: $35.00