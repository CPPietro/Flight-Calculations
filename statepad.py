class state():
    def __init__(self):
        # 0 = Metric 1 = Imperial
        self.units = 0
        self.empty_weight = 0
        self.total_fuel = 0
        self.wing_surface_area = 0
        self.fuel_weight = 0

    def setup_units(self):
        while True:
            print("Select unit system: 0 = Metric, 1 = Imperial")
            self.units = input("Enter choice: ")
            if self.units == "0" or "1":
                self.units = int(self.units)
                return
            else:
                print("Enter 0 for metric or 1 for imperial")


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
state_1.setup_units()