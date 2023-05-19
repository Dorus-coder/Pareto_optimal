import matplotlib.pyplot as plt



def generate_pareto_front(data):
    """
    Generate the Pareto front from a given dataset.
    Returns a list of indices representing the Pareto front.
    """
    pareto_front = []
    for i, point in enumerate(data):
        if not any(dominates(data[j], point) for j in pareto_front):
            pareto_front.append(i)
    return pareto_front

# Example data (two objectives)
data = [
    [1, 5],
    [3, 2],
    [2, 4],
    [4, 1],
    [5, 3],
    [6, 2],
    [3, 3],
    [4, 4],
]

pareto_front = generate_pareto_front(data)

# Plotting the Pareto front
x = [point[0] for point in data]
y = [point[1] for point in data]

plt.scatter(x, y, label='Points')
plt.scatter([x[i] for i in pareto_front], [y[i] for i in pareto_front], color='red', label='Pareto Front')
plt.xlabel('Objective 1')
plt.ylabel('Objective 2')
plt.title('Pareto Front')
plt.legend()
plt.show()
