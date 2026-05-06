# Calculates Lift via the lift equation
# rho = air pressure (Generaly QNH(hPa), but in this equation it is kg/m3)

# Imports state
from state import state_1

# Class for using the lift equation
class lift_equation():

    # Function for converting air pressure and surface area from imperial to metric
    def convert_imperial_to_metric(self, imp_rho, imp_surface_area):
        rho = imp_rho * 16.018
        surface_area = imp_surface_area / 10.764
        return rho, surface_area

    # Function that calculates lift from the parameters
    def calculate_lift(self, rho, velocity, surface_area, CL):
        # Full equation (metric)
        # Lift = (rho/2) x velocity2 x surface area x co-efficient of lift

        # Checks if params are givin in imperial and if they are converts them to metric
        if state_1.units == 1:
            rho, surface_area = self.convert_imperial_to_metric(rho, surface_area)

        # Simplifies the equation
        rho = rho / 2
        velocity = velocity ** 2

        # The equation after simplifying rho and velocity
        lift = rho * velocity * surface_area * CL

        return lift

    # For the get_lift_params function
    # Checks if input is blank and if so reverts to standard, otherwise converts to float
    def check_get_standard(self, input_str, metric_standard, imperial_standard):
        if state_1.units == 0:
            standard = metric_standard
        else:
            standard = imperial_standard
        if input_str.strip() == "":
            return standard
        else:
            try:
                return float(input_str)
            # Catches the error for if the user didn't input a num
            except ValueError:
                print("Must be a number! Reverting to standard")
                return standard

    # Gets the params/variable for the lift equation from the user
    def get_lift_params(self):
        print("Please enter following variables: ")
        print(f"Unit system = ")
        if state_1.units == 0:
            print("Metric")
        else:
            print("Imperial")
        print("(Leave blank for standard at 35,000ft)")

        #  Gets air presure - standard = 0.38kg/m3 at cruise(35,000ft)
        print("Enter air pressure (kg/m3 or lb/ft3): ")
        air_pressure = self.check_get_standard(input(), 0.38, 0.0237)

        # Gets velocity - standard = 230m/s (440kn)
        print("Enter velocity (Knots): ")
        velocity = self.check_get_standard(input(), 440, 440)
        # Converts knots to m/s
        velocity = velocity/1.944

        # Gets surface area of wing - standard = 122.6m2 for a320
        # Checks if wing surface area is already in the state
        if state_1.wing_surface_area == 0:
            print("Enter wing surface area: (m2 or ft2)")
            surface_area = self.check_get_standard(input(), 122.6, 1319.6554)
        else:
            print("Surface area loaded from current state")
            surface_area = state_1.wing_surface_area

        # Get co-efficent of lift - standard = 0.595
        cl = self.check_get_standard(input("Enter co-effiecnt of lift: "), 0.595, 0.595)

        return air_pressure, velocity, surface_area, cl

    # Main entry point
    def main(self):
        print("Lift calculator")

        # Gets parameters for the equation
        air_pressure, velocity, surface_area, cl = self.get_lift_params()

        # Completes the calculation
        lift = round(self.calculate_lift(air_pressure, velocity, surface_area, cl))

        print("Lift=")
    
        # Converts the output from metric to imperial if neccesary
        if state_1.units == 0:
            print(f"{lift}N")
        else:
            imp_lift = lift/4.448
            print(f"{imp_lift}lb-force")

        # Makes sure window doesn't close instantly
        input("Press enter to leave")
        return

if __name__ == "__main__":
    app = lift_equation()
    app.main()