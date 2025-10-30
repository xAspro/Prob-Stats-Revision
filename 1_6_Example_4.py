import numpy as np
import matplotlib.pyplot as plt

n = 25
trials = 10**4
ind = np.arange(n)

matches = 0
for _ in range(trials):
    perm = np.random.permutation(n)
    # print("i = ", _ , " perm = ", perm)
    if np.any(perm == ind):
        # print("perm = ", perm, " is selected")
        matches += 1

mean = matches / trials

# Anyway, beyond n = 20, the values dont change much. There is only the difference 
# due to floating point error
if n < 150: 
    dt = float
else: 
    dt = object
fact = np.cumprod(ind + 1, dtype=dt)
# print("factorial = ", fact)
anal_ans = np.sum((-1)**(ind) / fact)

print()
print("simulated probability is ", mean)
print()
print("Analytical answer is ", anal_ans)
print("difference = ", (mean - anal_ans))
print()
print("Analytical answer for n -> infinity is ", (1 - 1 / np.e))
print("difference = ", (mean - (1 - 1 / np.e)))
print()
print("difference between the differences is ", (anal_ans - (1 - 1 / np.e)))
