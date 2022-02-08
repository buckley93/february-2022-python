# camaro_car = {'make': 'Chevy', 'year': 2017, 'color': 'red'}
# civic = {'make': 'honda', 'year': 1992, 'color': 'white'}
# gtr = {'make': 'nissan', 'year': 2001, 'color': 'blue'}

# class Vehicle():
    # all_cars = []
    # def __init__(self, make, year, color):
    #     self.make = make
    #     self.year = year
    #     self.color = color
    #     Vehicle.all_cars.append(self)

    # def change_color(self, new_color):
    #     self.color = new_color
    #     return self

    # #instance Methods
    # def change_year(self, new_year):
    #     self.year = new_year
    #     return self

    # def print_car(self):
    #     print(f'make = {self.make}, year = {self.year}, color = {self.color}')
    #     return self

    # @classmethod
    # def print_all_cars(cls):
    #     for cars in cls.all_cars:
    #         cars.print_car()


# camaro = Vehicle('Chevy', 2017, ['black', 'yellow'])
# prius = Vehicle('Toyota', 2016, 'gunmetal gray')
# godzilla = Vehicle('Nissan', 1995, 'green')
# camaro.change_color('yellow').change_year(1997)
# camaro = Vehicle(camaro_car['make'], camaro_car['year'], camaro_car['color'])
# print(camaro.make)
# camaro.change_color('yellow')
# print(camaro.color[0])
# camaro.change_year(2020)
# print(camaro.year)
# Vehicle.print_all_cars()

class Dinner():
    all_dinners = []
    def __init__(self, main_course,sides,drink,dessert = 'tiramisu'):
        self.main_course = main_course
        self.sides = sides
        self.drink = drink
        self.dessert = dessert
        Dinner.all_dinners.append(self)

    def add_side(self, side):
        self.sides.append(side)
        return self

    def eat_dessert(self):
        self.dessert = None
        return self

    def print_dinner(self):
        print(f'main_course = {self.main_course}, sides = {self.sides}, drink = {self.drink}, dessert = {self.dessert}')

    @classmethod
    def print_all_dinners(cls):
        for dinners in cls.all_dinners:
            dinners.print_dinner()

dinner_1 = Dinner('spaghetti', ['meatballs, Garlic Bread'], 'red wine', 'tiramisu')
dinner_2 = Dinner('steak', 'potatoes', 'coke')
dinner_3 = Dinner('chicken', 'salad', 'sprint')
dinner_4 = Dinner('beef', 'brocolli', 'mt. dew')

# print(dinner_1.main_course)
# dinner_1.add_side('salad')
# print(dinner_1.sides)
# dinner_1.eat_dessert()
# print(dinner_1.dessert)
# print(print.sides)
# print(dinner_2.dessert)
Dinner.print_all_dinners()