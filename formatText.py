import pandas as pd

# Lee el CSV en un DataFrame
df = pd.read_csv("tu_archivo.csv")

# Selecciona las columnas necesarias
df = df[['host', 'user email', 'created']]

# Encuentra el ancho máximo de los valores en 'host' y 'user email'
max_host_len = df['host'].str.len().max()
max_user_email_len = df['user email'].str.len().max()

# Lista para almacenar el resultado formateado
formatted_list = []

# Itera sobre cada fila del DataFrame
for _, row in df.iterrows():
    # Formatea cada valor con el ancho correspondiente
    host = f"{row['host']:<{max_host_len}}"
    user_email = f"{row['user email']:<{max_user_email_len}}"
    created = row['created']
    
    # Crea la línea formateada y añádela a la lista
    formatted_line = f"{host} {user_email} {created}"
    formatted_list.append(formatted_line)

# Muestra el resultado
for line in formatted_list:
    print(line)
