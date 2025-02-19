shopping_cart_items = []


# finds average price of items in shopping cart list
def average_price(cart_items):
    try:
        # function scope
        average = 0

        for item in cart_items:
            # for loop scope
            average += item.price
        average = average / len(cart_items)
        return average
    except ZeroDivisionError as e:
        return average


average_price_of_cart_items = average_price(shopping_cart_items)

print(f"Your average cart item price is {average_price_of_cart_items} dollars")
