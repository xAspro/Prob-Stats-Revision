import numpy as np

def simulate_urn(n_col, n_tot, replace=False, weights=None, num_trial=1000):
    colour = [("X"+str(i)) for i in range(1, n_col+1)]

    if weights is None:
        weights = [1/n_col for _ in range(n_col)]

    n_balls = np.floor(np.array(weights) / np.sum(weights) * n_tot).astype(int)
    print("The balls in the urn are: ", dict(zip(colour, n_balls)))

    x2 = 0
    for _ in range(num_trial):
        urn = n_balls.copy()
        # print("Current urn: ", dict(zip(colour, urn)))
        counts = {c:0 for c in colour}

        for _ in range(np.sum(n_balls)):
            draw = np.random.choice(colour, p=urn/np.sum(urn))
            counts[draw] += 1

            if draw == "X2" and counts["X1"] == 0:
                # print("X2 is drawn before X1")
                # print("counts: ", counts)
                x2 += 1
                break

            if counts["X1"] > 0:
                break

            if not replace:
                urn[colour.index(draw)] -= 1
                urn = np.maximum(urn, 0)

    print(f"Probability that X2 is drawn before X1: {x2/num_trial}")


simulate_urn(3, 100, replace=False, weights=[0.25, 0.5, 0.25], num_trial=100000)
simulate_urn(3, 100, replace=True, weights=[0.25, 0.5, 0.25], num_trial=100000)