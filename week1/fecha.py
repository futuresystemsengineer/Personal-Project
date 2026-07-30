meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    fecha = input("Date: ").strip()
    if "/" in fecha:
        try:
            mes, dia, anio = fecha.split("/")
            mes =int(mes)
            dia =int(dia)
            anio =int(anio)
            if 1 <= mes <=12 and 1 <= dia <= 31:
                break
        except ValueError:
            pass
    elif "," in fecha:
        try:
            fecha_correcta = fecha.replace(",", "")
            mes, dia, anio = fecha_correcta.split(" ")
            mes = meses.index(mes.title()) + 1
            dia = int(dia)
            anio =int(anio)
            if 1 <= dia <= 31:
                break
        except IndexError:
            pass
print(f"{anio}-{mes:02}-{dia:02}")