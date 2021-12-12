import numpy as np
piles = {}
n = [1, 2, 3, 4, 5]
m = max(piles, key=lambda key: piles[key])

piles[9] = 8


c = max(piles, key=lambda x: piles[x]) if piles

print(c)
