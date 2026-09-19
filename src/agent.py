import random

class Agent: 
    def __init__(self, alelo1, alelo2):
        self.alelo1 = alelo1
        self.alelo2 = alelo2

    def get_size(self):
        if self.alelo1 == "A" and self.alelo2 == "A":
            size = 80
        elif self.alelo1 == "A" or self.alelo2 == "A":
            size = 65
        elif self.alelo1 == "a" and self.alelo2 == "a":
            size = 50

        return size
    
    def reproduce(self, partner):

        self_alelos = [self.alelo1, self.alelo2]
        self_alelo = random.choice(self_alelos)

        partner_alelos = [partner.alelo1, partner.alelo2]
        partner_alelo = random.choice(partner_alelos)

        new_agent = Agent(self_alelo, partner_alelo)

        return new_agent

agent1 = Agent("A", "a")
agent2 = Agent("A", "a")

print(agent1.get_size())
print(agent2.get_size())

agent3 = agent1.reproduce(agent2)

print(agent3.get_size())
