# from logic.temperature import Temperature


class Calorie:
    """
    Takes as an input information from the user and calculates
    the amount of calorie user must have in a day
    """
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.5 + self.height + 5 - self.temperature
        return result


# if __name__ == "__main__":
#     temperature = Temperature(country='kyrgyzstan', city='bishkek').get()
#     calorie = Calorie(weight=77, height=185, age=19, temperature=temperature)
#     print(calorie.calculate())
