import numpy as np
import matplotlib.pyplot as plt

n = 5000
p = np.linspace(0, 1, 100)

# 4 doors- 1 car, 1 book, 1 apple, 1 goat
# order of value is car > book > apple > goat
# Monty always reveals the lowest value item possible (not chosen by contestant)
# with probability p, and the second lowest value item with probability (1-p)

def monty_hall_simulation(p, trials=10000, condition_on_apple=False):
    debug = False

    wins = 0
    monty_reveals_apple = 0
    monty_reveals_apple_and_wins = 0
    for _ in range(trials):
        doors = np.random.choice(4, 4, replace=False) # 0: goat, 1: apple, 2: book, 3: car
        print("doors = ", doors) if debug else None
        contestant_choice = 0

        monty_options = [i for i in range(4) if i != contestant_choice]
        print("monty_options before sorting = ", monty_options)if debug else None
        monty_options.sort(key=lambda x: doors[x])  # Sort by value
        print("monty_options after sorting = ", monty_options)if debug else None
        reveal_choice = monty_options[0] if np.random.rand() < p else monty_options[1]
        print("reveal_choice = ", reveal_choice)if debug else None

        if condition_on_apple and doors[reveal_choice] == 1:  # Apple
            monty_reveals_apple += 1

        # Switching strategy
        remaining_doors = [i for i in range(4) if i != contestant_choice and i != reveal_choice]
        print("remaining_doors = ", remaining_doors)if debug else None
        contestant_choice = np.random.choice(remaining_doors)
        print("contestant_choice after switching = ", contestant_choice)if debug else None

        if doors[contestant_choice] == 3:  # Car
            print("Contestant wins a car!")if debug else None
            print("doors[contestant_choice] = ", doors[contestant_choice])if debug else None
            wins += 1

            if condition_on_apple and doors[reveal_choice] == 1:  # Apple
                monty_reveals_apple_and_wins += 1

    if condition_on_apple:
        return wins, trials, monty_reveals_apple, monty_reveals_apple_and_wins
    
    return wins, trials

def plot():

    switch_win_probs = []
    prob_monty_reveals_apple = []
    prob_monty_reveals_apple_and_wins = []

    analytical_win = np.full_like(p, 3/8, dtype=float)
    analytical_monty_reveals_apple = (2 - p) / 4
    analytical_monty_reveals_apple_and_wins = 1 / (2 * (2 - p))


    for prob in p:
        switch_wins, switch_trials, monty_reveals_apple, monty_reveals_apple_and_wins = monty_hall_simulation(prob, n, condition_on_apple=True)
        switch_win_probs.append(switch_wins / switch_trials)
        prob_monty_reveals_apple.append(monty_reveals_apple / switch_trials)
        prob_monty_reveals_apple_and_wins.append(monty_reveals_apple_and_wins / monty_reveals_apple if monty_reveals_apple > 0 else 0)

    plt.plot(p, switch_win_probs, label='Simulated Win', color='blue', linestyle='--')
    plt.plot(p, analytical_win, label='Analytical Win Solution', color='orange', linestyle='-.')
    plt.plot(p, prob_monty_reveals_apple, label='Simulated Monty Reveals Apple', color='green', linestyle='--')
    plt.plot(p, analytical_monty_reveals_apple, label='Analytical Monty Reveals Apple', color='red', linestyle='-.')
    plt.plot(p, prob_monty_reveals_apple_and_wins, label='Simulated Win given Monty Reveals Apple', color='purple', linestyle='--')
    plt.plot(p, analytical_monty_reveals_apple_and_wins, label='Analytical Win given Monty Reveals Apple', color='brown', linestyle='-.')

    plt.xlabel('Probability of Monty Revealing Lowest Value Item (p)')
    plt.ylabel('Probability of Winning Car')
    plt.title('Modified Monty Hall Problem with 4 Doors')
    plt.ylim(0, 1)

    # Used this while just plotting the win rates
    # plt.ylim(max(np.min(analytical_win) - 0.05, 0), min(np.max(analytical_win) + 0.05, 1))
    plt.legend()
    plt.grid()
    plt.show()

def print_results(prob, small_trials, condition_on_apple=False):
    big_trials = small_trials * 100
    result = monty_hall_simulation(prob, big_trials, condition_on_apple=condition_on_apple)
    switch_wins, switch_trials = result[0], result[1]

    print(f"\n\nMonty reveals lowest value item with probability {prob}:")
    print("Switching Strategy:")
    print("Total Wins:", switch_wins)
    print("Total Trials:", switch_trials)
    print("Winning Probability:", switch_wins / switch_trials)
    print("\nConditioned on Monty revealing an apple:\n" ) if condition_on_apple else None
    if condition_on_apple:
        monty_reveals_apple, monty_reveals_apple_and_wins = result[2], result[3]
        prob_reveal_apple = monty_reveals_apple / switch_trials
        conditional_prob_win_given_apple = monty_reveals_apple_and_wins / monty_reveals_apple if monty_reveals_apple > 0 else 0
        print("Total times Monty revealed an apple:", monty_reveals_apple)
        print("Total Wins when Monty revealed an apple:", monty_reveals_apple_and_wins)

        analytical_value_apple = (2 - prob) / 4
        analytical_value_win_given_apple = 1 / (2 * (2 - prob))
        lines = [
            f"Probability of Monty revealing an apple: {prob_reveal_apple}",
            f"Analytical Winning Probability given Apple: {analytical_value_apple}",

            f"Conditional Winning Probability: {conditional_prob_win_given_apple}",
            f"Correct (Analytical) Value:      {analytical_value_win_given_apple}",
        ]

        width = max(len(line) for line in lines)

        print("┌" + "─" * (width + 2) + "┐")
        for line in lines:
            print(f"│ {line.ljust(width)} │")
        print("└" + "─" * (width + 2) + "┘")



plot()
# print_results(0, n, condition_on_apple=True)
# print_results(0.5, n, condition_on_apple=True)
# print_results(1, n, condition_on_apple=True)





