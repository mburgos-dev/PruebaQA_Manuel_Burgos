import requests

url = "https://petstore.swagger.io/v2"
response = requests.get(f"{url}/pet/findByStatus?status=available")

if response.status_code == 200:
    mascotas = response.json()
    nombres_mascota = [mascota["name"] for mascota in mascotas]
    class ContadorMascotas:
        def __init__(self, nombres_mascotas):
            self.nombres_mascota = nombres_mascotas

        def contar_nombres(self):
            contador = {}
            for nombre in self.nombres_mascota:
                if nombre in contador:
                    contador[nombre] += 1
                else:
                    contador[nombre] = 1
            return contador

    contador_mascotas = ContadorMascotas(nombres_mascota)
    cuenta_nombre = contador_mascotas.contar_nombres()

    print("Conteo de mascotas por nombre:")
    print(cuenta_nombre)
else:
    print(f"Error al obtener la lista de mascotas: {response.status_code}")