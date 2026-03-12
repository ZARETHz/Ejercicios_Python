ventas = [
    ("Ana", "Enero", "Laptop", 2, 15000),
    ("Luis", "Enero", "Mouse", 10, 250),
    ("Ana", "Febrero", "Laptop", 1, 15000),
    ("Luis", "Febrero", "Teclado", 5, 800),
    ("Ana", "Enero", "Mouse", 3, 250)
]

ingresos = {}
for venta in ventas :
    empleado = venta [0]
    cantidad = venta [3]
    precio = venta [4]
    total = cantidad * precio
    
    if empleado in ingresos:
        ingresos[empleado] +=total
    else:
        ingresos[empleado] = total
        
    print(ingresos)
    
productos = set()
for venta in ventas:
    producto = venta[2]
    productos.add(producto)
    
print(productos)
    
ingresos_mes = {}

for venta in ventas:
    mes = venta[1]
    cantidad = venta[3]
    precio = venta[4]
    total = cantidad * precio
    
    if mes in ingresos_mes:
        ingresos_mes[mes] += total
    else:
        ingresos_mes[mes] = total
        
print(ingresos_mes)

mayor_ingreso = 0
mejor_empleado = ""
for empleadp in ingresos:
    if ingresos[empleadp] > mayor_ingreso:
        mayor_ingreso = ingresos[empleadp]
        mejor_empleado = empleadp
print(f"El mejor empleado es {mejor_empleado} con un ingreso de {mayor_ingreso}")
   