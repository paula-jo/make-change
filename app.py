from services import money


def main():
    going = True;
    while going:
        try:
            value = input("Please enter the amount you'd like to make change for:  ")
            print("You entered: " + value)
            money.make_change(float(value))
            going = False
        except ValueError:
            print("No letters or spaces please!")


main()

