#  List comprehensions
menu = ['pasta', 'pizza', 'salad', 'bread']
pizzas = [item for item in menu if item.lower() == 'pizza']

print(pizzas)  # Output: ['pizza']


# set comprehensions
favorite_tea = [
    "Masala Chai",
    "Ginger Tea",
    "Lemon Tea",
    "Masala Chai",
    "Green Tea",
    "Ginger Tea",  
]

unique_tea = {tea for tea in favorite_tea}

print(unique_tea)

recipes = {
    "pasta": ["tomato", "basil", "garlic"],
    "pizza": ["tomato", "cheese", "basil"],
    "salad": ["lettuce", "tomato", "cucumber"],
}

unique_ingredients = {ingredient for ingredients in recipes.values() for ingredient in ingredients}

print(unique_ingredients)

# Dictionary comprehensions

car_rates = {
    "Baleno": 1000000,
    "Swift": 800000,
    "Dzire": 900000,
    "Ertiga": 1100000,
}

car_prices_usd = {car: price/80 for car, price in car_rates.items()}

print(car_prices_usd)


#  Generator comprehensions (This is most memory efficient )
daily_sales = [1000, 2000, 3000, 4000, 5000]

above_expectation_sales = sum(sale for sale in daily_sales if sale > 3000)

print(above_expectation_sales)  # Output: <generator object <genexpr> at 0x7f9b8c0c1d30>
