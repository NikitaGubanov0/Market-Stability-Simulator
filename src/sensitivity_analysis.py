def sensitivity_analysis(market_data, parameters):
    results = {}
    for param, values in parameters.items():
        results[param] = []
        for value in values:
            updated_assets = deepcopy(market_data['assets'])
            updated_agents = deepcopy(market_data['agents'])

            if param == 'leverage':
                for agent in updated_agents:
                    agent.leverage = value
            elif param == 'transaction_tax':
                for asset in updated_assets:
                    asset.transaction_tax = value

            simulation_result = simulate_market(updated_agents, updated_assets, 100)
            results[param].append(analyze_market_data(simulation_result))

    return results
