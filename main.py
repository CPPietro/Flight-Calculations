
from state import state_1
from lift_equation import lift_equation

def print_help():
    print("Help: ")
    print("'q' = Quit")
    print("'lift' = Lift Equations")
    print("Press enter to return")
    input()
    return

def main():
    # Sets up chosen unit system
    state_1.setup_units()

    # Main loop
    while True:
        print()
        print("==== Flight Calculations ====")
        print()

        print("What would you like to do? (h for help)")
        user_in = input(":")
        if user_in == "h":
            print_help()
        elif user_in == "q":
            return
        elif user_in == "lift":
            print()
            print()
            lift = lift_equation()
            lift.main()
        else:
            print("Not an option, try again")

main()
