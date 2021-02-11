# Example of organising some sales data at a local pizza place. 

# Toppings available:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]

# Advertises the number of different toppings available
num_pizzas = len(toppings)
print(" We sell " + str(num_pizzas) +" "+ "different kinds of pizza topping!")

# Combines the pizza toppings list and pizza price list
pizzas = zip(prices, toppings)
pizzas = list(pizzas)

# Sorts the pizzas with the lowest price first and advertises the toppings available with costs
pizzas.sort()
print(pizzas)

# Example of some sales data for the pizza place

# Stores the cheapest pizza in a variable
cheapest_pizza = pizzas[0]
# Stores the most expensive of pizza in a variable
priciest_pizza = pizzas[-1]
# Stores the three cheapest pizzas in a variable
three_cheapest = pizzas[0:3]
# Review the number of $2 slices available
num_two_dollar_slices = prices.count(2)
