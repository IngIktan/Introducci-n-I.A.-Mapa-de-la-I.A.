# Daniel Alejandro Flores Sepulveda
# Programa para demostrar la Regla de la Cadena en una red bayesiana

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definición de la red bayesiana
modelo = BayesianModel([('A', 'B'), ('C', 'B'), ('B', 'D')])

# Asignación de probabilidades condicionales
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.7], [0.3]])
cpd_b = TabularCPD(variable='B', variable_card=2, 
                   values=[[0.3, 0.05, 0.9, 0.5],
                           [0.7, 0.95, 0.1, 0.5]],
                   evidence=['A', 'C'], evidence_card=[2, 2])
cpd_d = TabularCPD(variable='D', variable_card=2, 
                   values=[[0.9, 0.6],
                           [0.1, 0.4]],
                   evidence=['B'], evidence_card=[2])

# Agregamos los CPDs a la red bayesiana
modelo.add_cpds(cpd_a, cpd_c, cpd_b, cpd_d)

# Verificación de la consistencia de la red bayesiana
print("¿Es consistente la red bayesiana?", modelo.check_model())

# Realización de inferencia
inferencia = VariableElimination(modelo)
probabilidad_conjunta = inferencia.query(variables=['A', 'C', 'B', 'D'])

# Impresión de resultados
print("Probabilidad conjunta de A, C, B y D:")
print(probabilidad_conjunta)
