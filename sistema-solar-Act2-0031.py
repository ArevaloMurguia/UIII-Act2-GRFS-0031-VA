
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Arevalo Rafael NC:0031

# Crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 5 listas de planetas con 4 elementos por lista

mer = ['Mercurio', 57.9, False, 1631]
ven = ['Venus', 108.2, False, 1610]
tie = ['Tierra', 149.6, False, 0]
mar = ['Marte', 227.9, False, 1610]
jup = ['Júpiter', 778.5, True, 1610]

# Creamos una lista de listas (conformando la tabla)
lista_planetas = [mer, ven, tie, mar, jup]

print(lista_planetas)

# Utilizar pandas para organizar la tabla (DataFrame o marco de datos)
# A cada columna le ponemos nombre

df_planetas = pd.DataFrame(
    lista_planetas,
    columns=["Nombre", "Distancia", "Tiene_anillos", "Descubridor_año"]
)

print(df_planetas)

# Creamos el archivo CSV y lo guardamos en CSV
df_planetas.to_csv("sistema_solar.csv", index=False)

# Crear gráfica de líneas
# Donde X es Nombre en el eje horizontal
# Donde Y es Distancia al Sol en el eje vertical

plt.plot(df_planetas["Nombre"], df_planetas["Distancia"])
plt.title("Distancia de los planetas al Sol 0031")
plt.xlabel("Nombre de los planetas")
plt.ylabel("Distancia al Sol (Mkm)")
plt.show()

# Creamos una gráfica de puntos

plt.scatter(df_planetas["Nombre"], df_planetas["Distancia"])
plt.title("Planetas del Sistema Solar 0031")
plt.xlabel("Nombre de los planetas")
plt.ylabel("Distancia al Sol (Mkm)")
plt.show()

# Gráfica de barras

plt.bar(df_planetas["Nombre"], df_planetas["Distancia"])

# Etiquetas y título
plt.title("Distancia de los planetas al Sol 0031")
plt.xlabel("Planetas")
plt.ylabel("Distancia al Sol (Mkm)")

# Mostrar la gráfica
plt.show()

# Ordenar la gráfica de barras de manera descendente
# Del planeta más lejano al más cercano

df_planetas_ordenar = df_planetas.sort_values(
    "Distancia", ascending=False
)

plt.bar(
    df_planetas_ordenar["Nombre"],
    df_planetas_ordenar["Distancia"]
)
plt.title("Planetas ordenados por distancia 0031")
plt.show()

# Coloreando la gráfica

df_planetas_ordenar = df_planetas.sort_values(
    "Distancia", ascending=False
)

plt.bar(
    df_planetas_ordenar["Nombre"],
    df_planetas_ordenar["Distancia"],
    color=["b", "g", "c", "m", "y"]
)
plt.title("Sistema Solar a color 0031")
plt.xlabel("Planetas")
plt.ylabel("Distancia al Sol (Mkm)")
plt.show()

# Gráfica de pastel

plt.pie(
    df_planetas["Distancia"],
    labels=df_planetas["Nombre"],
    autopct="%1.1f%%"
)
plt.title("Distancia de los planetas al Sol 0031")
plt.show()

print("+-+-+-+- Arevalo Rafael NC:0031 +-+-+-+-+")