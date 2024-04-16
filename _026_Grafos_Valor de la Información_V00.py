# Daniel Alejandro Flores Sepulveda
# Programa en Python para calcular el Valor de la Información en una Red de Decisión

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definición de la estructura de la red de decisión
modelo = BayesianModel([('A', 'D'), ('B', 'D')])

# Definición de las tablas de probabilidad condicional (CPD)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.1, 0.3, 0.8, 0.9], [0.9, 0.7, 0.2, 0.1]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Añadir las tablas CPD al modelo
modelo.add_cpds(cpd_a, cpd_b, cpd_d)

# Crear un objeto de VariableElimination para realizar inferencias
inferencia = VariableElimination(modelo)

# Calcular la utilidad esperada antes de obtener información sobre la variable A
utilidad_esperada_inicial = inferencia.query(variables=['D'])

# Calcular la utilidad esperada después de obtener información sobre la variable A
modelo_informacion_a = modelo.copy()
modelo_informacion_a.remove_edges_from([('B', 'D')])  # Eliminar la influencia de B en D
utilidad_esperada_con_a = inferencia.query(variables=['D'])

# Calcular el Valor de la Información para la variable A
valor_informacion_a = utilidad_esperada_inicial.values[1] - utilidad_esperada_con_a.values[1]

print("Valor de la Información para la variable A:", valor_informacion_a)
