class state():
    def __init__(self):
        # 0 = Metric 1 = Imperial
        units = 0
        empty_weight = 0
        total_fuel = 0
        wing_surface_area = 0
        fuel_weight = 0

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