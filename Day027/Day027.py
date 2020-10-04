def get_order(order):
    menu = "Burger Fries Chicken Pizza Sandwich Onionrings Milkshake Coke".split()
    res = ""
    for item in menu:
        if item.casefold() in order:
            for i in range(0, order.count(item.casefold())):
                res += item + " "
    return res[:-1]

get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza")
                    # "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"
get_order("pizzachickenfriesburgercokemilkshakefriessandwich")
                    # "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke"