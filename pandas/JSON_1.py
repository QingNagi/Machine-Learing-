import pandas as pd
import numpy as np
G = pd.DataFrame({'tom': [10, 20, 8], 'Jack': [28, 48, 38]})
print(G)
G.to_json('j1.json')
G.to_json('j2.json', orient='table')

print(pd.read_json('j1.json'))