logs = [
    ("192.168.1.1", "/home", "Chrome"),
    ("192.168.1.2", "/login", "Firefox"),
    ("192.168.1.1", "/dashboard", "Chrome"),
    ("192.168.1.3", "/home", "Edge"),
    ("192.168.1.2", "/home", "Firefox")
]

urls_por_ip = {}

for registro in logs:
    ip = registro[0]
    url = registro[1]

    if ip in urls_por_ip:
        urls_por_ip[ip].add(url)
    else:
        urls_por_ip[ip] = {url}

print(urls_por_ip)

visitas_por_url = {}

for registro in logs:
    url = registro[1]

    if url in visitas_por_url:
        visitas_por_url[url] += 1
    else:
        visitas_por_url[url] = 1

print(visitas_por_url)


uso_navegador = {}

for registro in logs:
    navegador = registro[2]

    if navegador in uso_navegador:
        uso_navegador[navegador] += 1
    else:
        uso_navegador[navegador] = 1

max_uso = 0
navegador_mas_usado = ""

for navegador in uso_navegador:
    if uso_navegador[navegador] > max_uso:
        max_uso = uso_navegador[navegador]
        navegador_mas_usado = navegador

print("Navegador más utilizado:", navegador_mas_usado)

ips_unicas = set()

for registro in logs:
    ips_unicas.add(registro[0])

lista_ips_ordenadas = sorted(ips_unicas)

print(lista_ips_ordenadas)
