import random
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt

class MarketModel(Model):
    def __init__(self, num_agents, width, height):
        self.num_agents = num_agents
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.datacollector = DataCollector(
            model_reporters={"AssetValue": lambda m: m.compute_total_asset_value()},
            agent_reporters={"AssetValue": lambda a: a.asset_value},
        )
        self.order_book = []

        # Создание агентов
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
        self.is_buy = True

    def step(self):
        # Выбор случайной стратегии
        strategy = random.choice(["random", "sequential"])
        if strategy == "random":
            self.random_strategy()
        elif strategy == "sequential":
            self.sequential_strategy()

    def random_strategy(self):
        # Создание ордера на основе случайной стратегии
        asset_type = random.choice(["A", "B", "C"])
        price = random.uniform(50, 200)
        quantity = random.randint(1, 5)
        is_buy = random.choice([True, False])

        order = Order(self.unique_id, asset_type, price, quantity, is_buy)
        self.model.order_book.append(order)

    def sequential_strategy(self):
        # Создание ордера на основе последовательной стратегии
        asset_type = "A"
        price = 100
        quantity = 1
        self.is_buy = not self.is_buy

        order = Order(self.unique_id, asset_type, price, quantity, self.is_buy)
        self.model.order_book.append(order)


class Order:
    def __init__(self, agent_id, asset_type, price, quantity, is_buy):
        self.agent_id = agent_id
        self.asset_type = asset_type
        self.price = price
        self.quantity = quantity
        self.is_buy = is_buy


# Запуск симуляции
num_agents = 100
width = 10
height = 10
model = MarketModel(num_agents, width, height)

for i in range(1000):
    model.step()

# Графики
agent_asset_values = model.datacollector.get_agent_vars_dataframe()
model_asset_value = model.datacollector.get_model_vars_dataframe()

plt.figure()
plt.plot(model_asset_value["AssetValue"])
plt.title("Total Asset Value")
plt.xlabel("Step")
plt.ylabel("Value")
plt.show()

plt.figure()
plt.boxplot([agent_asset_values.xs(i, level=1)["AssetValue"] for i in range(num_agents)])
plt.title("Agent Asset Value Distribution")
plt.xlabel("Agent ID")
plt.ylabel("Asset Value")
plt.show()
