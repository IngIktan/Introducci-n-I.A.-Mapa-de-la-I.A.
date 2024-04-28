# Autor: Daniel Alejandro Flores Sepulveda
# Este programa genera tablas de verdad para operaciones lógicas AND y OR.

# Función para generar una tabla de verdad para el operador AND
def truth_table_and():
    table = [(p, q, p and q) for p in [True, False] for q in [True, False]]
    return table

# Función para generar una tabla de verdad para el operador OR
def truth_table_or():
    table = [(p, q, p or q) for p in [True, False] for q in [True, False]]
    return table

# Imprimir la tabla de verdad para el operador AND
print("Tabla de Verdad para AND:")
print("p | q | p and q")
print("-" * 13)
for p, q, result in truth_table_and():
    print(f"{int(p)} | {int(q)} | {int(result)}")

# Imprimir la tabla de verdad para el operador OR
print("\nTabla de Verdad para OR:")
print("p | q | p or q")
print("-" * 12)
for p, q, result in truth_table_or():
    print(f"{int(p)} | {int(q)} | {int(result)}")
