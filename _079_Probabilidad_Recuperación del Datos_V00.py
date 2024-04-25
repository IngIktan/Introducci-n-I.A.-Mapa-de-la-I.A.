# Autor: Daniel Alejandro Flores Sepulveda
# Este programa realiza recuperación de datos de una base de datos SQLite.

import sqlite3

# Conectamos con la base de datos (si no existe, se crea automáticamente)
conn = sqlite3.connect('sample.db')

# Creamos un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Creamos una tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, position TEXT)''')

# Insertamos algunos datos de ejemplo
cursor.execute("INSERT INTO employees (name, age, position) VALUES (?, ?, ?)", ('John Doe', 30, 'Manager'))
cursor.execute("INSERT INTO employees (name, age, position) VALUES (?, ?, ?)", ('Jane Smith', 25, 'Developer'))

# Guardamos los cambios
conn.commit()

# Ejecutamos una consulta para recuperar todos los empleados
cursor.execute("SELECT * FROM employees")

# Obtenemos los resultados de la consulta
results = cursor.fetchall()

# Mostramos los resultados
print("Datos de empleados:")
for row in results:
    print(row)

# Cerramos la conexión
conn.close()
