# Calculates Lift via the lift equation
# rho = air pressure (Generaly QNH(hPa), but in this equation it is kg/m3)

class lift_equation():

    def calculate_lift(self, rho, velocity, surface_area, CL):
        # Lift = (rho/2) x velocity2 x surface area x co-efficient of lift

        # Simplifies the equation
        rho = rho / 2
        velocity = velocity ** 2

        # The equation after simplifying rho and velocity
        lift = rho * velocity * surface_area * CL

        return lift

    # For the get_lift_params function
    # Checks if input is blank and if so reverts to standard, otherwise converts to float
    def check_get_standard(self, input_str, standard):
        if input_str.strip() == "":
            return standard
        else:
            try:
                return float(input_str)
            except ValueError:
                print("Must be a number! Reverting to standard")
                return standard

    # Gets the params/variable for the lift equation from the user
    def get_lift_params(self):
        print("Please enter following variables: ")
        print("(Leave blank for standard at 35,000ft)")

        #  Gets air presure - standard = 0.38kg/m3 at cruise(35,000ft)
        air_pressure = self.check_get_standard(input("Enter air pressure (kg/m3): "), 0.38)

        # Gets velocity - standard = 230m/s (440kn)
        velocity = self.check_get_standard(input("Enter speed (m/s): "), 230)

        # Gets surface area of wing - standard = 122.6m2 for a320
        surface_area = self.check_get_standard(input("Enter surface area of wing(m2): "), 122.6)

        # Get co-efficent of lift - standard = 0.595
        cl = self.check_get_standard(input("Enter co-effiecnt of lift: "), 0.595)

        return air_pressure, velocity, surface_area, cl

    # Main entry point
    def main(self):
        print("Lift calculator")

        # Gets parameters for the equation
        air_pressure, velocity, surface_area, cl = self.get_lift_params()

        # Completes the calculation
        lift = round(self.calculate_lift(air_pressure, velocity, surface_area, cl))

        print("Lift=")
        print(f"{lift}N")
        input("Press enter to leave")
        return

if __name__ == "__main__":
    app = lift_equation()
    app.main()