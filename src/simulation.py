import random

from agent import Agent, Genome


class Population:

    def __init__(self, agents):
        self.agents = agents

    def genotype_counts(self):

        AA = 0
        Aa = 0
        aa = 0

        for agent in self.agents:

            alelos = agent.genome.alelos

            if alelos[0] == "A" and alelos[1] == "A":
                AA += 1

            elif alelos[0] == "a" and alelos[1] == "a":
                aa += 1

            else:
                Aa += 1

        return AA, Aa, aa

    def genotype_frequencies(self):

        AA, Aa, aa = self.genotype_counts()

        total = len(self.agents)

        if total == 0:
            return {
                "AA": 0,
                "Aa": 0,
                "aa": 0
            }

        return {
            "AA": AA / total,
            "Aa": Aa / total,
            "aa": aa / total
        }

    def allele_frequencies(self):

        AA, Aa, aa = self.genotype_counts()

        total = len(self.agents)

        if total == 0:
            return {
                "A": 0,
                "a": 0
            }

        A = (2 * AA + Aa) / (2 * total)
        a = (Aa + 2 * aa) / (2 * total)

        return {
            "A": A,
            "a": a
        }

    def reproduce(self, offspring_count=None):

        if len(self.agents) < 2:
            raise ValueError(
                "A population needs at least two agents to reproduce."
            )

        if offspring_count is None:
            offspring_count = len(self.agents)

        offspring = []

        for _ in range(offspring_count):

            parent_1, parent_2 = random.sample(self.agents, 2)

            child = parent_1.reproduce(parent_2)

            offspring.append(child)

        return Population(offspring)


class Simulation:

    def __init__(self, population):
        self.population = population
        self.generation = 0

    def step(self):

        self.population = self.population.reproduce()
        self.generation += 1

    def run(self, generations):

        for _ in range(generations):

            self.step()

            print(
                f"Generation {self.generation}: "
                f"{len(self.population.agents)} agents"
            )

            print(
                "  Genotypes:",
                self.population.genotype_counts()
            )

            print(
                "  Alleles:",
                self.population.allele_frequencies()
            )


def create_initial_population(size):

    agents = []

    for _ in range(size):

        genome = Genome([
            random.choice(["A", "a"]),
            random.choice(["A", "a"])
        ])

        agents.append(Agent(genome))

    return Population(agents)


if __name__ == "__main__":

    population = create_initial_population(100)

    simulation = Simulation(population)

    print("Initial population:")
    print("  Genotypes:", population.genotype_counts())
    print("  Genotype frequencies:", population.genotype_frequencies())
    print("  Allele frequencies:", population.allele_frequencies())

    print()

    simulation.run(20)