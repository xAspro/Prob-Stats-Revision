import numpy as np
import matplotlib.pyplot as plt

# def run_robberies(num_people, weight_non_loser, weight_loser, num_robberies): 
#     weights = np.full(num_people, weight_non_loser, dtype=float) 
#     weights[0] = weight_loser 
#     weights /= np.sum(weights) 
#     loser = np.zeros(num_people) 
    
#     for i in range(num_robberies): 
#         if i % 1000 == 0: 
#             print(f"Running robbery {i}/{num_robberies}") 
#         wt = weights.copy() 
        
#         for pos in range(num_people): 
#             chosen_index = np.random.choice(num_people, p=wt/np.sum(wt)) 
#             if chosen_index == 0: 
#                 loser[pos] += 1 
#                 break 
#             wt[chosen_index] = 0 

#     print("w = ", weight_non_loser, "v = ", weight_loser)
#     print("loser:", loser) 
#     print("Loser sum", np.sum(loser))
#     if np.sum(loser) != num_robberies:
#         print("Warning: Total robberies does not match total loser count.")
#     return loser

def run_robberies(num_people, weight_non_loser, weight_loser, num_robberies):
    weights = np.full(num_people, weight_non_loser, dtype=float)
    weights[0] = weight_loser
    weights /= np.sum(weights)

    loser = np.zeros(num_people)

    for i in range(num_robberies):
        # if i % 1000 == 0:
        #     print(f"Running robbery {i}/{num_robberies}")
        wt = weights.copy()

        permutation = np.random.choice(num_people, size=num_people, p=wt, replace=False)

        mask = permutation == 0
        loser[mask] += 1


    print("w = ", weight_non_loser, "v = ", weight_loser)
    print("loser:", loser)
    if np.sum(loser) != num_robberies:
        print("Warning: Total robberies does not match total loser count.")

    return loser

def analytical_solution(num_people, w, v):
    P = np.zeros(num_people)
    for i in range(num_people):
        if i == 0:
            P[i] = v / (v + (num_people - 1) * w)
        else:
            prod_terms = ((num_people - np.arange(1, i + 1)) * w) / (v + (num_people - np.arange(1, i + 1)) * w)
            P[i] = np.prod(prod_terms) * (v / (v + (num_people - i - 1) * w))
    return P
    

def plot_histogram(num_people, loser, analytical, title='Distribution of Loser Index for Uniform Weights'):
    plt.bar(range(num_people), loser/np.sum(loser))
    plt.plot(range(num_people), analytical, 'r-', label='Analytical Solution')
    plt.xlabel('Loser Index')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid()
    plt.show()

def main():
    num_people = 200
    num_robberies = 200000


    # set weight of loser here
    # w = weight of non losers
    # v = weight of loser
    w = 1
    v = 1

    loser = run_robberies(num_people, w, v, num_robberies)
    analytical = analytical_solution(num_people, w, v)
    plot_histogram(num_people, loser, analytical)

    w = 1
    v = 4

    loser = run_robberies(num_people, w, v, num_robberies)
    analytical = analytical_solution(num_people, w, v)
    plot_histogram(num_people, loser, analytical, title='Distribution of Loser Index for Weighted Weights with v=4 and w=1')

    w = 4
    v = 1

    loser = run_robberies(num_people, w, v, num_robberies)
    analytical = analytical_solution(num_people, w, v)
    plot_histogram(num_people, loser, analytical, title='Distribution of Loser Index for Weighted Weights with v=1 and w=4')

if __name__ == "__main__":
    main()

    


