# Birthday Problem

import matplotlib.pyplot as plt
import random

def birthday_problem(num_peop, num_trial):
    # First calculates Analytical solution and then Simulated solution
    prob_inv = 1
    for i in range(num_peop):
        prob_inv *= (365 - i) / 365

    analytical_prob = 1 - prob_inv

    success_cases = 0

    for i in range(num_trial):
        birthdays = []
        for i in range(num_peop):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                success_cases += 1
                break
            birthdays.append(birthday)

    simulated_prob = success_cases / num_trial

    return analytical_prob, simulated_prob

def plot_birthday_problem(num_peop, num_trial):
    people = list(range(1, num_peop + 1))
    anal_prob, sim_prob = zip(*[birthday_problem(peop, num_trial) for peop in people])

    plt.plot(people, sim_prob, marker='o', label='Simulation')
    plt.plot(people, anal_prob, marker='x', label='Analytical', color='red')
    plt.axhline(0.5, color='green', linestyle='--', label='50% Probability')
    plt.title("Birthday Paradox: Simulation vs Analytical")
    plt.xlabel("Number of People")
    plt.ylabel("Probability of Shared Birthday")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    num_peop = 100
    num_trial = 1000

    plot_birthday_problem(num_peop, num_trial)
