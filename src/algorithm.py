import numpy as np


def obj_function(solution, areas):
    profit = np.zeros_like(solution)
    for i, area in enumerate(areas):
        for j, column in enumerate(area.columns):
            profit[i][j] = sum(area[column][:int(solution[i][j])])
    return profit.sum()


def sum_supplies(solution, supplies):
    sum = 0
    for categorie, supply in enumerate(supplies):
        sum+=int(solution[:,categorie].sum() > supply)
    return sum


def generate_neighbor(solution):
    area1 = np.random.randint(0, solution.shape[0])
    area2 = np.random.randint(0, solution.shape[0])

    category = np.random.randint(0, solution.shape[1])

    max_bikes_to_move = min(solution[area1, category], solution[area2, category])
    bikes_to_move = np.random.randint(1, max_bikes_to_move + 2)

    neighbor_solution = np.copy(solution)
    neighbor_solution[area1, category] -= bikes_to_move
    neighbor_solution[area2, category] += bikes_to_move

    return np.clip(neighbor_solution, 0, None)


def simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations, areas, supplies):
    current_solution = initial_solution
    current_temperature = initial_temperature

    for i in range(num_iterations):
        current_profit = obj_function(current_solution, areas)

        neighbor_solution = generate_neighbor(current_solution)
        neighbor_profit = obj_function(neighbor_solution, areas)

        profit_difference = neighbor_profit - current_profit

        if profit_difference > 0 or np.random.rand() < np.exp(profit_difference / current_temperature):
            if sum_supplies(neighbor_solution, supplies) == 0:
                current_solution = neighbor_solution

        current_temperature *= cooling_rate

    return current_solution


def relocate_bicycles(initial_solution, initial_temperature, cooling_rate, num_iterations, areas, supplies, show_results=True):
    best_solution = simulated_annealing(initial_solution.astype(float), initial_temperature, cooling_rate, num_iterations, areas, supplies)
    profit = obj_function(best_solution, areas)

    if show_results == True:
        print("Valor objetivo ótimo (Lucro esperado):", profit)
        print("\nSolução ótima:")
        for i in range(best_solution.shape[0]):
            for j in range(best_solution.shape[1]):
                if best_solution[i][j] != 0:
                    print(f"Número de bicicletas da categoria {j + 1} a serem movidas para a área {i + 1}: {best_solution[i][j]}")

    return profit, best_solution
