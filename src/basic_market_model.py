import random
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

class MarketModel(Model):
    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            model_reporters={"TotalAssetValue": lambda m: m.compute_total_asset_value()},
            agent_reporters={"AssetValue": lambda a: a.asset_value},
        )

        for i in range(self.num_agents):
            initial_asset_value = random.randint(100, 1000)
            agent = MarketAgent(i, self, initial_asset_value)
            self.schedule.add(agent)

            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

    def compute_total_asset_value(self):
        return sum([agent.asset_value for agent in self.schedule.agents])

class MarketAgent(Agent):
    def __init__(self, unique_id, model, initial_asset_value):
        super().__init__(unique_id, model)
        self.asset_value = initial_asset_value

    def step(self):
        # Здесь должны быть реализованы стратегии торговли и другие действия агента
        pass

# Запуск симуляции
num_agents = 100
width = 10
height = 10
model = MarketModel(num_agents, width, height)

for i in range(1000):
    model.step()
