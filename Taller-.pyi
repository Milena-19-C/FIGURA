import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"

# Nombres de las columnas (según la documentación del UCI)
column_names = [
    'Sexo', 'Longitud', 'Diametro', 'Alto', 'Whole_weight',
    'Shucked_weight', 'Viscera_weight', 'Shell_weight', 'Rings'
]

abalone = pd.read_csv(url, header=None, names=column_names)

# Imprimir las primeras 5 filas (cabecera)
print("Cabecera del dataset Abalone:")
print(abalone.head())


























