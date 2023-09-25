import requests

url = "https://petstore.swagger.io/v2"
crear_usuario = f"{url}/user"
obtener_usuarios = f"{url}/user/"

nuevo_usuario = {
    "id": 1,
    "username": "mi_usuario",
    "firstName": "Juan",
    "lastName": "Español",
    "email": "correo@example.com",
    "phone": "1234567890"
}
response = requests.post(crear_usuario, json=nuevo_usuario)

if response.status_code == 200:
    print("Usuario creado exitosamente.")
else:
    print("Error al crear el usuario.")

username = nuevo_usuario["username"]
user_data_response = requests.get(f"{obtener_usuarios}{username}")

if user_data_response.status_code == 200:
    user_data = user_data_response.json()
    print("Datos del usuario:")
    print(user_data)
else:
    print("Error al obtener los datos del usuario.")