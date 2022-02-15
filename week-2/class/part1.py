# how do we build a function

# def car_info(make, model, year=1996):
#     # print(make)
#     # print(model)
#     print(year)
#     return f"i like {make} {model} from the year {year}"
    
# # print(car_info(model = "Corvette", make = "Chevrolet", year=2008))
# car1 = car_info(model = "Corvette", make = "Chevrolet", year=2008)
# print(car1)

# import random

# print(round(random.random() * 50))

# create a function that helps an employee decide how much to put into a 401k between 0 and 100. if the amount is even print the amount is even else print it is odd. then return the amount

# def amount_to_be_added():
#     amount = round(random.random() * 100)

#     if amount % 2 == 0:
#         print(f"{amount} is even")

#     else:
#         print(f"{amount} is odd")
#     return amount

# print(amount_to_be_added())

# dictionaries

sports_cars = {
    'Chevrolet': 'Corvette',
    'Nissan': 'GTR',
    'Ford': 'GT'
}

# print(sports_cars)
# print('Nissan')
# print(sports_cars['Nissan'])
# print(sports_cars['Nissan'])
# sports_cars['Toyota'] = "Supra"

# print(sports_cars)

# for in loop

# for car in sports_cars:
#     print(sports_cars[car])

# .keys()
# for car in sports_cars.keys():
#     print(car)

# .values() 
# for car in sports_cars.values():
#     print(car)

# .items()
# for unicorn, banana in sports_cars.items():
#     print(unicorn, banana)