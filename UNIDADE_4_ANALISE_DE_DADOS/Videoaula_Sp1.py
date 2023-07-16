import pandas as pd
import numpy as np
cliente = {"Nome": ['Marcelo', 'Ana', 'Maria'],
           "Idade": [33, 26, 45],
           "Telefone": [999999999, 111111111, 555555555, ]}

df = pd.DataFrame(cliente)
print(df)
print()
print(df.Nome)
print()
print(df.Idade.mean())
print()

s = pd.Series(("Carla", "Lis"), index=['03', '07'])
print(s)