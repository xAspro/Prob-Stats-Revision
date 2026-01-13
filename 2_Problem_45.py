import numpy as np
import matplotlib.pyplot as plt

n = 5000
p = np.linspace(0, 1, 500)

def monty_hall_simulation(p, trials=10000):
    wins = 0
    monty_open_2 = 0
    monty_opens_2_and_wins = 0
    for _ in range(trials):
        doors = np.random.choice(2, 3, p=[1 - p, p])

        contestant_choice = 0

        monty_options = [i for i in range(3) if i != contestant_choice and doors[i] == 0]

        if len(monty_options) == 0:
            # Monty doesnt have a goat in the options to reveal
            continue
        monty_opens = np.random.choice(monty_options)


        # Switching strategy
        remaining_doors = [i for i in range(3) if i != contestant_choice and i != monty_opens]
        contestant_choice = remaining_doors[0]


        if monty_opens == 1:
            monty_open_2 += 1

        if doors[contestant_choice] == 1:
            wins += 1
            if monty_opens == 1:
                monty_opens_2_and_wins += 1

    return wins, trials, monty_open_2, monty_opens_2_and_wins


def plot():

    switch_win_conditional_probs = []
    y_switch = 2 * p / (1 + p)

    for prob in p:
        _, _, switch_monty_open_2, switch_monty_open_2_and_wins = monty_hall_simulation(prob, n)

        switch_win_conditional_probs.append(switch_monty_open_2_and_wins / switch_monty_open_2 if switch_monty_open_2 > 0 else 0)

    plt.plot(p, switch_win_conditional_probs, label='Monty Opens 2 to reveal Goat', color='green', linestyle='--')
    plt.plot(p, y_switch, label='Theoretical solution', color='orange', linestyle='-.')
    plt.xlabel('Probability of Car Behind a Door (p)')
    plt.ylabel('Probability of Winning')
    plt.title('Modified Monty Hall Problem with Car in each door with probability p')
    plt.legend()
    plt.grid()
    plt.show()

switch_wins, switch_trials, switch_monty_open_2, switch_monty_open_2_and_wins = monty_hall_simulation(0.5, n)
print("Switching Strategy:")
print("Total Wins:", switch_wins)
print("Total Trials:", switch_trials)
print("Probability of Winning when Switching:", switch_wins / switch_trials)
print("Monty opened door 2 times:", switch_monty_open_2)
print("Monty opened door 2 and contestant won:", switch_monty_open_2_and_wins)
print("Probability of Winning given Monty opened door 2:", switch_monty_open_2_and_wins / switch_monty_open_2 if switch_monty_open_2 > 0 else 0)

plot()
