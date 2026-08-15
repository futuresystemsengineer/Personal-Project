registro = [
    {"nombre": "Gianluca", "carrera": "ingenieria", "nota": 18},
    {"nombre": "Maria", "carrera": "medicina", "nota": 15},
    {"nombre": "Carlos", "carrera": "ingenieria", "nota": 8},
    {"nombre": "Sofia", "carrera": "ingenieria", "nota": 16},
    {"nombre": "Jose", "carrera": "medicina", "nota": 9}
]

# Llamada a la función:
# evaluar_carrera(registro, "ingenieria")
def evaluar_carrera(estudiantes, carrera_buscada):
    aprobados = []
    total_notas = 0
    total_estudiantes = 0
    for x in estudiantes:
        if x["carrera"] == carrera_buscada:
            total_estudiantes += 1
            total_notas += x["nota"]
            if x["nota"] >= 10:
                aprobados.append(x["nombre"])
    if total_estudiantes >0:
        promedio = total_notas / total_estudiantes
    else:
        promedio =0
    return {"aprobados": aprobados, "promedio": promedio}

evaluar = evaluar_carrera(registro, "derecho")
print(evaluar)