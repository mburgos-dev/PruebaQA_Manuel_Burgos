import requests

url = "https://petstore.swagger.io/v2/pet/findByStatus?status=sold"
response = requests.get(url)

if response.status_code == 200:
    mascotas = response.json()
    for mascota in mascotas:
        if 'name' in mascota:
            print(f"ID: {mascota['id']}, Nombre: {mascota['name']}")
        else:
            print(f"Elemento sin clave 'name': {mascota}")
else:
    print(f"Error al obtener las mascotas vendidas: {response.status_code}")

