from services import money
from services.money import currencies


def main():
    value = input("Please enter the amount you'd like to make change for:  ")
    print("You entered: " + value)
    money.make_change(value)

    for quantity in currencies:
        if currencies[quantity] > 0:
            print(f"{currencies[ quantity ]} x ${quantity}.")


main()

