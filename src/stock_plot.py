import matplotlib.pyplot as plt
import pandas as pd

# Загрузите результаты симуляции в DataFrame
results_df = pd.DataFrame(simulation_results)

# Создайте графики и таблицы на основе результатов симуляции
plt.plot(results_df["time"], results_df["price"])
plt.xlabel("Time")
plt.ylabel("Price")
plt.title("Price Evolution")

plt.figure()
plt.plot(results_df["time"], results_df["trading_volume"])
plt.xlabel("Time")
plt.ylabel("Trading Volume")
plt.title("Trading Volume Evolution")

plt.show()

statistics_df = results_df.describe()
print(statistics_df)

results_df.to_csv("simulation_results.csv")
statistics_df.to_csv("simulation_statistics.csv")