# Daniel Alejandro Flores Sepulveda
# Ejemplo de Red Bayesiana Dinámica en Python utilizando pgmpy

# Daniel Alejandro Flores Sepulveda
# Ejemplo de Red Bayesiana Dinámica en Python utilizando pgmpy

from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD

# Definir la estructura de la DBN
dbn = DBN()

# Definir las variables en cada paso de tiempo
dbn.add_edges_from([
    (('X', 0), ('X', 1)),  # Variable X en el paso de tiempo t depende de X en t-1
    (('X', 0), ('Y', 1)),  # Variable Y en el paso de tiempo t depende de X en t-1
    (('X', 1), ('Y', 1)),  # Variable Y en el paso de tiempo t depende de X en t
])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_x0 = TabularCPD(variable=('X', 0), variable_card=2, values=[[0.6], [0.4]])
cpd_x1 = TabularCPD(variable=('X', 1), variable_card=2, values=[[0.3, 0.7], [0.7, 0.3]], evidence=[('X', 0)],
                    evidence_card=[2])
cpd_y1 = TabularCPD(variable=('Y', 1), variable_card=2, values=[[0.2, 0.4, 0.7, 0.9], [0.8, 0.6, 0.3, 0.1]],
                    evidence=[('X', 0), ('X', 1)], evidence_card=[2, 2])

# Añadir las CPDs a la DBN
dbn.add_cpds(cpd_x0, cpd_x1, cpd_y1)

# Verificar la validez de la DBN
print("¿Es válida la Red Bayesiana Dinámica?", dbn.check_model())

# Imprimir la estructura de la DBN
print("Estructura de la Red Bayesiana Dinámica:")
print(dbn.edges())

