def run_simulation(num_agents, initial_conditions, asset_characteristics, regulation_params):
    model = MarketModel(num_agents, initial_conditions, asset_characteristics, regulation_params)
    for i in range(1000):
        model.step()
    return model.datacollector

def compare_scenarios(results_1, results_2):
    agent_asset_values_1 = results_1.get_agent_vars_dataframe()
    agent_asset_values_2 = results_2.get_agent_vars_dataframe()

    # Вычислите среднее значение активов агентов для каждого сценария
    avg_asset_value_1 = agent_asset_values_1["AssetValue"].mean()
    avg_asset_value_2 = agent_asset_values_2["AssetValue"].mean()

    print("Average asset value for scenario 1:", avg_asset_value_1)
    print("Average asset value for scenario 2:", avg_asset_value_2)

# Задайте разные сценарии с различными параметрами
scenario_1 = {
    "num_agents": 100,
    "initial_conditions": {"width": 10, "height": 10},
    "asset_characteristics": {"price": 100, "quantity": 10},
    "regulation_params": {"capital_requirement": 10, "leverage_limit": 5, "transaction_tax": 0.01}
}

scenario_2 = {
    "num_agents": 200,
    "initial_conditions": {"width": 20, "height": 20},
    "asset_characteristics": {"price": 100, "quantity": 10},
    "regulation_params": {"capital_requirement": 20, "leverage_limit": 10, "transaction_tax": 0.02}
}

# Запустите симуляцию для каждого сценария
results_1 = run_simulation(**scenario_1)
results_2 = run_simulation(**scenario_2)

# Сравните результаты двух сценариев и выведите разницу в ключевых метриках
compare_scenarios(results_1, results_2)
