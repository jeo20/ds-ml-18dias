import json

jsonString = '{"cuentaUsuarios": 2,"usuarios":[{"nombre": "usuario1","online": true},{"nombre": "usuario2","online": false}]}'

jsonDecode = json.loads(jsonString)
print(jsonDecode)

print(jsonDecode["cuentaUsuarios"])
usuarios = jsonDecode["usuarios"]
print(usuarios)

#Acceder a los usuarios a través del array
usuario1 = usuarios[0]
usuario2 = usuarios[1]

print(usuario1["nombre"]+ ", " + str(usuario1["online"]))
print(usuario2["nombre"]+ ", " + str(usuario2["online"]))

#recorrer array de usuarios
for usuario in usuarios:
    print(str( usuario["nombre"]) +", "+ str(usuario["online"]))

