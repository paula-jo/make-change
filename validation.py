def money_validation(user_input):
    parsed_input = 0
    try:
        parsed_input = float(user_input)
    except ValueError:
        return {
            "is_valid": False,
            "reason": "No spaces or letters please. I only know how to float!"
        }
    if parsed_input < 0:
        return {
            "is_valid": False,
            "reason": "Sorry, I can't handle any negativity. Maybe try something positive next time!"
        }
    if parsed_input != round(parsed_input, 2):
        return {
            "is_valid": False,
            "reason": "Too many decimal places for me!"
        }
    return {
        "is_valid": True,
        }
