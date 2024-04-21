import numpy as np
import pyomo.environ as pyEnv

def relocate_bicycles(matrix, a, s, T, show_results=True):
    model = pyEnv.ConcreteModel()

    # índices para as áreas, categorias e bicicletas
    model.I = pyEnv.Set(initialize=range(matrix.shape[0]))
    model.J = pyEnv.Set(initialize=range(matrix.shape[1]))
    model.K = pyEnv.Set(initialize=range(matrix.shape[2]))

    # variáveis de decisão
    model.x = pyEnv.Var(model.I, model.J, model.K, domain=pyEnv.Binary, initialize=0)

    # função objetivo
    model.profit = pyEnv.Objective(
        expr=sum(matrix[i, j, k] * model.x[i, j, k] for i in model.I for j in model.J for k in model.K),
        sense=pyEnv.maximize
    )
    
    ## restrições
    # disponibilidade
    def supply_constraint(model, j):
        return sum(model.x[i, j, k] for i in model.I for k in model.K) <= a[j]

    model.supply_constraint = pyEnv.Constraint(model.J, rule=supply_constraint)

    # capacidade
    def capacity_constraint(model):
        return sum(s[j] * model.x[i, j, k] for i in model.I for j in model.J for k in model.K) <= T

    model.capacity_constraint = pyEnv.Constraint(rule=capacity_constraint)

    # condicional
    def sequential_constraint_rule(model, i, j, k):
        if k == 0:
            return pyEnv.Constraint.Skip
        else:
            return model.x[i, j, k] <= model.x[i, j, k-1]

    model.sequential_constraint = pyEnv.Constraint(model.I, model.J, model.K, rule=sequential_constraint_rule)

    # resolver o modelo
    solver = pyEnv.SolverFactory('glpk')
    results = solver.solve(model)
    
    # solução final
    sum_x = np.array([[sum(model.x[i, j, k].value for k in model.K) for j in model.J] for i in model.I])

    # mostra os resultados
    if show_results == True:
        print("Status:", results.solver.termination_condition)
        print("Valor objetivo ótimo (Lucro esperado):", pyEnv.value(model.profit))
        print("\nSolução ótima:")
        for i in model.I:
            for j in model.J:
                if sum_x[i][j] != 0:
                    print(f"Número de bicicletas da categoria {j + 1} a serem movidas para a área {i + 1}: {sum_x[i][j]}")

    return pyEnv.value(model.profit), sum_x