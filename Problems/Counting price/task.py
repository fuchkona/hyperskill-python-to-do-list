def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper  


@price_string
def new_price(current_price):
    return current_price * 0.9
