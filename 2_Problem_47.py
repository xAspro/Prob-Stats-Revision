import numpy as np
import matplotlib.pyplot as plt
from itertools import product

n = 4  # Number of doors

def monty(doors, remaining_doors, contestant_choice, switch=False):
    monty_options = [i for i in range(len(doors)) if i != contestant_choice and i in remaining_doors and doors[i] != 1]  # Monty cannot reveal the car
    reveal_choice = np.random.choice(monty_options)
    remaining_doors.remove(reveal_choice)
    if switch:
        contestant_choice = np.random.choice([d for d in remaining_doors if d != contestant_choice])
    return contestant_choice, remaining_doors


def monty_hall_simulation(strategy, num_doors=4, num_trials=10000):
    # print("strategy = ", strategy)
    # print("num_doors = ", num_doors)
    # print("\n\n\n\n")
    wins = 0
    for _ in range(num_trials):
        doors = np.zeros(num_doors  )
        doors[np.random.randint(num_doors)] = 1

        contestant_choice = 0
        remaining_doors = np.arange(num_doors).tolist()

        # Monty reveals two doors
        for i in range(num_doors - 2):
            # print("Round ", i + 1)
            # print("doors = ", doors)
            # print("contestant_choice = ", contestant_choice)
            # print("remaining_doors = ", remaining_doors)
            # print("switch = ", strategy[i])
            # print()
            contestant_choice, remaining_doors = monty(doors, remaining_doors, contestant_choice, switch=strategy[i])

        # print("\ndoors = ", doors)
        # print("contestant_choice = ", contestant_choice)
        # print("remaining_doors = ", remaining_doors)
        # print("\n\n")
        
        if doors[contestant_choice] == 1:  # Car
            wins += 1

    return wins / num_trials


def print_all_strategies(num_doors=4):
    # Generate all possible strategies, ie. combinations of switch/stay decisions
    strategies = list(product([True, False], repeat=num_doors - 2))


    for strategy in strategies:
        prob = monty_hall_simulation(strategy, num_doors=num_doors)
        strategy_str = ', '.join(['Switch' if s else ' Stay ' for s in strategy])
        print(f"Strategy ({strategy_str}): Probability of winning = {prob}")

print_all_strategies(n)



# Method 2

# If the prior probabilities of car being behind each door is not equal,
# then the formula would be
# Pl2 = (1 / (k - 1)) * Pl1 / ((1 / (k - 1)) * Pl1 + 1 / (k - 2) * (1 - Pl1 - Pj1))
# and
# Pi2 = (1 / (k - 2)) * Pi1 / ((1 / (k - 1)) * Pl1 + 1 / (k - 2) * (1 - Pl1 - Pj1))
# Pj2 = 0
# where Pl1 is the prior probability of car being behind door l (the door chosen by contestant)
# Pi1 is the prior probability of car being behind door i (one of the 
# remaining doors not chosen by contestant or revealed by monty)
# Pj1 is the prior probability of car being behind door j (the door revealed by monty)
# k is the number of remaining doors

# In the case of equal prior probabilities, Pl1 = Pi1 = Pj1
# We have,
# Pi1 = Pj1 = (1 - Pl1) / (k - 1)
# Substituting these values in the above equation, we get
# Pl2 = Pl1
# Pi2 = (1 - Pl1) / (k - 2)
# Pj2 = 0

def posterior_probabilities(prior_probs, revealed_door_index, contestant_choice_index):
    n = len(prior_probs)
    k = np.count_nonzero(prior_probs)
    pl1 = prior_probs[contestant_choice_index]
    pj1 = prior_probs[revealed_door_index]
    mask = (prior_probs != 0) & ~np.isin(np.arange(n), [contestant_choice_index, revealed_door_index])
    print("\nmask = ", mask)
    print("prior_probs = ", prior_probs)
    print("prior_probs != 0 = ", prior_probs != 0)
    
    posterior = np.zeros(n)
    print("posterior before updating others = ", posterior)

    den = (1 / (k - 1)) * pl1 + ((1 / (k - 2)) * (1 - pl1 - pj1))
    posterior[contestant_choice_index] = (1 / (k - 1)) * pl1 / den
    print("posterior after updating contestant choice = ", posterior)
    posterior[mask] = (1 / (k - 2)) * prior_probs[mask] / den
    print("posterior after updating others = ", posterior)

    return posterior

def test_posterior_probabilities():
    prior_probs = np.array([0.25, 0.25, 0.25, 0.25])
    revealed_door_index = 1
    contestant_choice_index = 0

    posterior = posterior_probabilities(prior_probs, revealed_door_index, contestant_choice_index)
    print("Posterior probabilities:", posterior)

    prior_probs = posterior
    contestant_choice_index = 2
    revealed_door_index = 3
    posterior = posterior_probabilities(prior_probs, revealed_door_index, contestant_choice_index)
    print("Posterior probabilities:", posterior)

test_posterior_probabilities()

# Analytically deriving for the expected value is not the right approach here,
# since the contestant's choice and Monty's choice is random among the remaining doors.
# Hence simulating the entire process is the correct way to estimate the probabilities.
# Each case, the evolution of the probabilities will be different based on the choices made.