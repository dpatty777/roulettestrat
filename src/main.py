from roulette_strat import roulette_simulation

# Run simulation
if __name__ == "__main__":
    spins = 100  # Number of spins to simulate
    total_profit, average_profit, file_name = roulette_simulation(spins=spins)
    print(f"Simulation completed for {spins} spins.")
    print(f"Total Profit: {total_profit}")
    print(f"Average Profit per Spin: {average_profit}")
    print(f"Results saved to: {file_name}")