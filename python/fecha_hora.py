import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()

# Sumar 5 días
fecha_mas_5_dias = fecha_hora_actual + datetime.timedelta(days=5)

# Restar 10 días
fecha_menos_10_dias = fecha_hora_actual - datetime.timedelta(days=10)

print("Fecha actual:", fecha_hora_actual)
print("Fecha dentro de 5 días:", fecha_mas_5_dias)
print("Fecha hace 10 días:", fecha_menos_10_dias)
