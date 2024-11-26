import numpy as np
import pandas as pd
from data import roulette_numbers

def roulette_simulation(spins=100):
    # Define all possible bets dynamically
    bets = {
        "zero": 10,
        "first_12": 50,
        "second_12": 0,
        "third_12": 50,
        "number": 0,  # Specific number bet
        "2_1_col1": 0,  # Bet on first column (2:1 payout)
        "2_1_col2": 0,  # Bet on second column (2:1 payout)
        "2_1_col3": 0,  # Bet on third column (2:1 payout)
        "red": 0,  # Bet on red
        "black": 50,  # Bet on black
        "even": 0,  # Bet on even numbers
        "odd": 0,  # Bet on odd numbers
        "high": 0,  # Bet on high numbers (19-36)
        "low": 0,  # Bet on low numbers (1-18)
    }

    # Total bet dynamically calculated
    total_bet = sum(bets.values())

    # Define payouts
    payouts = {
        "zero": 35,
        "first_12": 2,
        "second_12": 2,
        "third_12": 2,
        "number": 35,
        "2_1_col1": 2,
        "2_1_col2": 2,
        "2_1_col3": 2,
        "red": 1,
        "black": 1,
        "even": 1,
        "odd": 1,
        "high": 1,
        "low": 1,
    }

    # Results storage
    results = []

    # Simulate spins
    for _ in range(spins):
        # Randomly select a number (0-36)
        spin_number = np.random.randint(0, 37)
        spin_properties = roulette_numbers[spin_number]  # Lookup properties of the number

        # Default profit: Lose all bets
        profit = -total_bet

        # Evaluate bets based on spin properties
        if spin_number == 0 and bets["zero"] > 0:
            profit += bets["zero"] * payouts["zero"]

        if spin_properties["dozen"] == 1 and bets["first_12"] > 0:
            profit += bets["first_12"] * payouts["first_12"]

        if spin_properties["dozen"] == 2 and bets["second_12"] > 0:
            profit += bets["second_12"] * payouts["second_12"]

        if spin_properties["dozen"] == 3 and bets["third_12"] > 0:
            profit += bets["third_12"] * payouts["third_12"]

        if spin_properties["column"] == 1 and bets["2_1_col1"] > 0:
            profit += bets["2_1_col1"] * payouts["2_1_col1"]

        if spin_properties["column"] == 2 and bets["2_1_col2"] > 0:
            profit += bets["2_1_col2"] * payouts["2_1_col2"]

        if spin_properties["column"] == 3 and bets["2_1_col3"] > 0:
            profit += bets["2_1_col3"] * payouts["2_1_col3"]

        if spin_properties["color"] == "red" and bets["red"] > 0:
            profit += bets["red"] * payouts["red"]

        if spin_properties["color"] == "black" and bets["black"] > 0:
            profit += bets["black"] * payouts["black"]

        if spin_properties["even"] and bets["even"] > 0:
            profit += bets["even"] * payouts["even"]

        if not spin_properties["even"] and bets["odd"] > 0:
            profit += bets["odd"] * payouts["odd"]

        if spin_properties["high"] and bets["high"] > 0:
            profit += bets["high"] * payouts["high"]

        if not spin_properties["high"] and bets["low"] > 0:
            profit += bets["low"] * payouts["low"]

        # Append profit to results
        results.append(profit)

    # Create DataFrame for results
    results_df = pd.DataFrame(results, columns=["Profit"])

    # Summarize results
    total_profit = results_df["Profit"].sum()
    average_profit = results_df["Profit"].mean()

    # Save results to csv
    results_df.to_csv("roulette_simulation_results.xlsx", index=False)

    return total_profit, average_profit, "roulette_simulation_results.xlsx"

