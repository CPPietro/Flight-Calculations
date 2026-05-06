
# Class for the state currently open, holds data for all scripts
class state():
    # Initiates variables
    def __init__(self):
        # 0 = Metric 1 = Imperial
        self.units = 0
        self.empty_weight = 0
        self.total_fuel = 0
        self.wing_surface_area = 0
        self.fuel_weight = 0

    # Makes sure you have your preffered units set up
    def setup_units(self):
        while True:
            print("Select unit system: 0 = Metric, 1 = Imperial")
            self.units = input("Enter choice: ")
            try:
                self.units = int(self.units)
                return
            except ValueError:
                print("Invalid choice!")
                print()
                print()
                print("Enter 0 for metric or 1 for imperial")


    # Lets the scripts update fuel weight from updated fuel volume
    def update_fuel_weight(self):
        if self.total_fuel == 0:
            print("ERROR - Fuel still equals zero")
            return 1
        else:
            if self.units == 0:
                self.fuel_weight = self.total_fuel * 0.8
            else:
                self.fuel_weight = self.total_fuel * 6.7


state_1 = state()
