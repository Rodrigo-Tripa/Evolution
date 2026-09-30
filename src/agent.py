import random


class Genome:

    def __init__(self, alelos):
        self.alelos = alelos

    def get_alelo(self):
        return random.choice(self.alelos)

    def mutate(self, mutation_rate):

        mutation_prob_1 = random.random()
        mutation_prob_2 = random.random()

        if mutation_rate > mutation_prob_1:
            if self.alelos[0] == "A":
                self.alelos[0] = "a"
            elif self.alelos[0] == "a":
                self.alelos[0] = "A"

        if mutation_rate > mutation_prob_2:
            if self.alelos[1] == "A":
                self.alelos[1] = "a"
            elif self.alelos[1] == "a":
                self.alelos[1] = "A"


class Phenotype:

    def __init__(self, genome):

        self.genome = genome

        standard_deviation = 4

        if self.genome.alelos[0] == "A" and self.genome.alelos[1] == "A":
            expected_size = 80

        elif self.genome.alelos[0] == "A" or self.genome.alelos[1] == "A":
            expected_size = 65

        elif self.genome.alelos[0] == "a" and self.genome.alelos[1] == "a":
            expected_size = 50

        self.size = random.gauss(expected_size, standard_deviation)

class Agent:

    def __init__(self, genome):
        self.genome = genome
        self.phenotype = Phenotype(genome)

    def reproduce(self, partner):

        self_alelo = self.genome.get_alelo()
        partner_alelo = partner.genome.get_alelo()

        new_genome = Genome([
            self_alelo,
            partner_alelo
        ])

        new_genome.mutate(0.1)

        return Agent(new_genome)

