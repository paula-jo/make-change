from services import validation

currencies = {
    100.00: 0,
    50.00: 0,
    20.00: 0,
    10.00: 0,
    5.00: 0,
    1.00: 0,
    .25: 0,
    .10: 0,
    .05: 0,
    .01: 0
}


def make_change(entered_value):
    validation_result = validation.money_validation(entered_value)
    if not validation_result["is_valid"]:
        print(validation_result["reason"])
        return validation_result["reason"]

    entered_value = float(entered_value)

    for currency in currencies.keys():
        x = entered_value % currency
        currencies[currency] = (entered_value - x) / currency
        entered_value = entered_value - currencies[currency] * currency

    return currencies
