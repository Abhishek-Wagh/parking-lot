class ParkingLot:
    def __init__(self):
        self.spots = {}
        for i in range(1, 41):
            level = 'A' if i <= 20 else 'B'
            self.spots[i] = {'level': level, 'vehicle_number': None}
    
    def assign_spot(self, vehicle_number):
        for i in range(1, 41):
            if self.spots[i]['vehicle_number'] is None:
                self.spots[i]['vehicle_number'] = vehicle_number
                return {'level': self.spots[i]['level'], 'spot': i}
        return None
    
    def retrieve_spot(self, vehicle_number):
        for i in range(1, 41):
            if self.spots[i]['vehicle_number'] == vehicle_number:
                return {'level': self.spots[i]['level'], 'spot': i}
        return None

# create a new parking lot
parking_lot = ParkingLot()

# assign a spot to a new vehicle
assign_vehicle_number = str(input("Enter vehicle number to assign parking lot: "))
assigned_spot = parking_lot.assign_spot(assign_vehicle_number)
if assigned_spot:
    print(f"Assigned spot: {assigned_spot}")
else:
    print("Sorry, parking lot is full.")

# retrieve spot of a vehicle
retrieve_vehicle_number = str(input("Enter vehicle number to retrieve vehicle: "))
spot = parking_lot.retrieve_spot(retrieve_vehicle_number)
if spot:
    print(f"Vehicle is parked at: {spot}")
else:
    print("Vehicle not found.")