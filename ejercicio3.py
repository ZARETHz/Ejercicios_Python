inventario = [
    {"producto": "Laptop", "categoria": "Electrónica", "stock": 5},
    {"producto": "Mouse", "categoria": "Electrónica", "stock": 25},
    {"producto": "Silla", "categoria": "Muebles", "stock": 2},
    {"producto": "Escritorio", "categoria": "Muebles", "stock": 0}
]

productos_por_categoria = {}

for item in inventario:
    categoria = item["categoria"]
    producto = item["producto"]

    if categoria in productos_por_categoria:
        productos_por_categoria[categoria].append(producto)
    else:
        productos_por_categoria[categoria] = [producto]

print(productos_por_categoria)

productos_agotados = set()

for item in inventario:
    if item["stock"] == 0:
        productos_agotados.add(item["producto"])

print(productos_agotados)

productos_bajo_stock = []

for item in inventario:
    if item["stock"] < 5:
        productos_bajo_stock.append(item["producto"])

productos_bajo_stock = tuple(productos_bajo_stock)

print(productos_bajo_stock)

total_por_categoria = {}

for item in inventario:
    categoria = item["categoria"]

    if categoria in total_por_categoria:
        total_por_categoria[categoria] += 1
    else:
        total_por_categoria[categoria] = 1

print(total_por_categoria)
