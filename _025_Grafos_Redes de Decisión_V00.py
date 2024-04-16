# Daniel Alejandro Flores Sepulveda
# Ejemplo de implementación de una Red de Decisión en Python utilizando la biblioteca pgmpy

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Definición de la estructura de la red de decisión
modelo = BayesianModel([('A', 'C'), ('B', 'C')])

# Definición de las tablas de probabilidad condicional (CPD)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.1, 0.2, 0.3, 0.4], [0.9, 0.8, 0.7, 0.6]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Añadir las tablas CPD al modelo
modelo.add_cpds(cpd_a, cpd_b, cpd_c)

# Verificar si la red de decisión es válida
print("¿Es la red de decisión válida?", modelo.check_model())

# Imprimir la estructura de la red de decisión
print("Estructura de la red de decisión:")
print(modelo.edges())

# Imprimir las tablas de probabilidad condicional
print("\nTablas de Probabilidad Condicional:")
for cpd in modelo.get_cpds():
    print(cpd)
