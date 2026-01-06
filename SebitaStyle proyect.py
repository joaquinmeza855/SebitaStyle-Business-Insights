import pandas as pd # Importar la librería pandas para manipulación de datos
import matplotlib.pyplot as plt # Importar matplotlib para realizar las gráficas
import seaborn as sns # Importar seaborn para mejorar el estilo visual y mapas de calor
import numpy as np # Importar numpy para operaciones numéricas si fuera necesario

# --- 1. CONFIGURACIÓN E INGRESO DE DATOS --- #
precio_corte = 8000 # Definir el precio por corte ($8.000)

# Datos de recaudación mensual
datos_mensuales = { # Crear un diccionario con los datos de cortes por mes
    'Mes': ['Mes 1', 'Mes 2', 'Mes 3', 'Mes 4', 'Mes 5', 'Mes 6', 'Mes 7', 'Mes 8', 'Mes 9', 'Mes 10 (Parcial)'], # Lista de meses
    'Cortes': [91, 131, 115, 117, 113, 114, 125, 100, 114, 94] # Lista de cortes totales por mes
} # Cerrar el diccionario
df_mes = pd.DataFrame(datos_mensuales) # Convertir el diccionario en un DataFrame de pandas
df_mes['Ingreso'] = df_mes['Cortes'] * precio_corte # Calcular el ingreso multiplicando cortes por precio

# Datos por día de la semana
datos_dias = { # Crear diccionario para el análisis por día
    'Dia': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'], # Días analizados
    'Cortes': [102, 154, 158, 185, 240, 275] # Cortes acumulados en 39 semanas
} # Cerrar el diccionario
df_dias = pd.DataFrame(datos_dias) # Crear DataFrame de días
df_dias['Promedio'] = df_dias['Cortes'] / 39 # Calcular el promedio diario (39 semanas)

# Datos de franjas horarias
datos_horas = { # Crear diccionario para el análisis de horarios
    'Hora': ['18:00', '17:00', '17:30', '16:30', '19:00', '18:30', '19:30'], # Franjas horarias pico
    'Cortes': [89, 84, 83, 79, 79, 73, 69] # Volumen de cortes por hora
} # Cerrar el diccionario
df_horas = pd.DataFrame(datos_horas) # Crear DataFrame de horas

# --- 2. GENERACIÓN DE VISUALIZACIONES --- #

# Gráfico 1: Recaudación Mensual
plt.figure(figsize=(10, 6)) # Definir el tamaño de la figura para el gráfico mensual
sns.barplot(x='Mes', y='Ingreso', data=df_mes, palette='viridis') # Crear gráfico de barras de ingresos
plt.title('Recaudación Mes a Mes (SebitaStyle)') # Agregar título al gráfico
plt.xticks(rotation=45) # Rotar las etiquetas del eje X para mejor lectura
plt.ylabel('Ingreso en $') # Agregar etiqueta al eje Y
plt.show() # Mostrar el primer gráfico

# Gráfico 2: Frecuencia por Franja Horaria
plt.figure(figsize=(12, 6)) # Definir tamaño para el gráfico de barras horarias
sns.barplot(x='Hora', y='Cortes', data=df_horas, palette='magma') # Crear gráfico de barras de demanda horaria
plt.title('Frecuencia Total de Cortes por Franja Horaria (Pico de Demanda)') # Título del gráfico
plt.xlabel('Franja Horaria') # Etiqueta eje X
plt.ylabel('Cortes Totales Acumulados') # Etiqueta eje Y
plt.show() # Mostrar el segundo gráfico

# Gráfico 3: Mapa de Calor (Heatmap) - Reconstrucción de la matriz
dias_semana = ['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO'] # Definir cabeceras de días
horas_lista = ['09:30', '10:00', '11:00', '12:00', '16:30', '17:00', '18:00', '19:00', '20:00'] # Definir filas de horas
matriz_data = [ # Crear lista de listas con los valores de la matriz de calor del PDF
    [1, 3, 3, 4, 4, 5], # 09:30
    [0, 4, 3, 3, 5, 11], # 10:00
    [0, 3, 7, 3, 6, 17], # 11:00
    [1, 3, 5, 4, 5, 16], # 12:00
    [14, 14, 14, 14, 20, 15], # 16:30
    [14, 14, 11, 17, 21, 22], # 17:00
    [17, 20, 13, 20, 18, 24], # 18:00
    [15, 17, 13, 18, 11, 20], # 19:00
    [10, 12, 3, 10, 11, 5]  # 20:00
] # Cerrar matriz
df_heatmap = pd.DataFrame(matriz_data, index=horas_lista, columns=dias_semana) # Crear DataFrame para el mapa de calor

plt.figure(figsize=(10, 8)) # Definir tamaño del mapa de calor
sns.heatmap(df_heatmap, annot=True, cmap='YlGnBu', fmt='d') # Generar el heatmap con anotaciones numéricas
plt.title('Matriz de Calor: Frecuencia de Cortes por Día y Hora') # Título del heatmap
plt.show() # Mostrar el mapa de calor

# --- 3. RESUMEN DE MÉTRICAS CLAVE --- #
print(f"Cortes Totales: {df_mes['Cortes'].sum()}") # Imprimir la sumatoria total de cortes (1.114)
print(f"Recaudación Total: ${df_mes['Ingreso'].sum():,}") # Imprimir la recaudación total con formato de miles
print(f"Día con mayor promedio: {df_dias.loc[df_dias['Cortes'].idxmax(), 'Dia']}") # Identificar el día con más demanda