# Chapter 1, Problem 40

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb as C, factorial as fact

n = 10
k = 5

balls = np.arange(1, n + 1)

def sampling():
    sample = np.random.choice(balls, size=k, replace=True)
    return sample

def is_strictly_increasing(sample):
    return np.all(np.diff(sample) > 0)

def is_increasing(sample):
    return np.all(np.diff(sample) >= 0)

def simulate(runs=10000000):
    strictly_increasing_count = 0
    increasing_count = 0

    for _ in range(runs):
        sample = sampling()
        if is_strictly_increasing(sample):
            strictly_increasing_count += 1
            increasing_count += 1
            continue
        if is_increasing(sample):
            increasing_count += 1

    p_strictly_increasing = strictly_increasing_count / runs
    p_increasing = increasing_count / runs

    return p_strictly_increasing, p_increasing

def analytical_prob():
    p_strictly_increasing = C(n, k) / (n**k)
    p_increasing = C(n + k - 1, k) / (n**k)
    return p_strictly_increasing, p_increasing

p_strictly_increasing, p_increasing = simulate()
analytical_estimate_strictly_increasing, analytical_estimate_increasing = analytical_prob()

print("Estimated Probability of strictly increasing sequence:", p_strictly_increasing)
print("Analytical Probability of strictly increasing sequence:", analytical_estimate_strictly_increasing)
print("Estimated Probability of increasing sequence:", p_increasing)
print("Analytical Probability of increasing sequence:", analytical_estimate_increasing)