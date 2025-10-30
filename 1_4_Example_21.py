# Newton Pepys Problem

import numpy as np
import matplotlib.pyplot as plt

def at_least_m_sixes(m_values, runs=60000):
    prob = []
    for m in m_values:
        tot = 6 * m

        # To make the calculations easy, 6 is considered 1 and all the rest 0
        # Probabilities are chosen accordingly
        sum = np.sum(np.random.choice(2, size=(runs, tot), replace=True, p=[5/6, 1/6]), axis=1)
        mask = sum >= m
        p = np.sum(mask) / runs

        print("Probability for m = ", m, " is ", p)
        prob.append(p)
    
    return np.array(prob)


    
# m_values = np.arange(10) + 1
m_values = np.array([5, 10, 50, 100, 500, 1000])
p_values = at_least_m_sixes(m_values)

mask = p_values[1:] >= p_values[:-1]
mask = np.concatenate(([False], p_values[1:] >= p_values[:-1]))

print("mask = ", mask)

plt.plot(m_values, p_values, marker='o')

plt.scatter(m_values[mask], p_values[mask], color='r', zorder=5)
plt.xlabel("Number of 6s")
plt.ylabel("Probability")
plt.title("Probability of at least 1/6th 6s")
plt.show()
