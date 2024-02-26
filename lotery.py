import numpy as np

def weighted_lottery (weights):
    list_container=[]
    for clave, valor in weights.items():
        for _ in range(valor):
            list_container.append(clave)
    return np.random.choice(list_container) 

other_weights = {
        'winning': 1,
        'break_even': 2,
        'losing': 3
    }

print(weighted_lottery(other_weights))

