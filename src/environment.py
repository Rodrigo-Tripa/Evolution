class Environment:

    def __init__(self, food):

        self.food_available = food

    def get_food_per_individual(self, population_size):

        if population_size > 0:

            individual_food = self.food_available / population_size

            return individual_food

        else:

            individual_food = None

            return individual_food