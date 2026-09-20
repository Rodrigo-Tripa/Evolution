import random

class Genome:
    def __init__(self, alelos):
        self.alelos = alelos

class Agent: 
    def __init__(self, genome):
        self.genome = genome

    def get_size(self):
        if self.genome.alelos[0] == "A" and self.genome.alelos[1] == "A":
            size = 80
        elif self.genome.alelos[0] == "A" or self.genome.alelos[1] == "A":
            size = 65
        elif self.genome.alelos[0] == "a" and self.genome.alelos[1] == "a":
            size = 50

        return size
    
    def reproduce(self, partner):

        self_alelo = random.choice(self.genome.alelos)

        partner_alelo = random.choice(partner.genome.alelos)

        new_genome = Genome([self_alelo, partner_alelo])

        new_agent = Agent(new_genome)

        return new_agent

genome1 = Genome(["A", "a"])
agent1 = Agent(genome1)

genome2 = Genome(["A", "a"])
agent2 = Agent(genome2)

print(agent1.get_size())
print(agent2.get_size())

agent3 = agent1.reproduce(agent2)

print(agent3.get_size())
