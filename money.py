currencies = {
    .01: 0,
    .05: 0,
    .10: 0,
    .25: 0,
    1.00: 0,
    5.00: 0,
    10.00: 0,
    20.00: 0,
    50.00: 0,
    100.00: 0
}

ordered_denominations = sorted(currencies.keys())

ordered_denominations.reverse()


def make_change(entered_value):

    if entered_value < 0:
        print("Sorry, I need a positive value!")
        return "Sorry, I need a positive value!"

    for currency in ordered_denominations:
        x = entered_value % currency
        currencies[currency] = (entered_value - x) / currency
        entered_value = entered_value - currencies[currency] * currency

    print("You'll need: ")

    for quantity in currencies:
        if currencies[quantity] > 0:
            print(f"{currencies[quantity]} x ${quantity}.")

