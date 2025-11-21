import re
from datos import cargar_usuarios, guardar_usuarios

def email_valido(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def buscar_por_correo(correo):
    usuarios = cargar_usuarios()
    correo = correo.strip().lower()
    for u in usuarios:
        if u.get("correo") == correo:
            return u
    return None

def registrar(correo, contrasena):
    correo = correo.strip().lower()
    if not email_valido(correo):
        return False, "Correo inválido"
    if buscar_por_correo(correo):
        return False, "Correo ya registrado"
    usuarios = cargar_usuarios()
    usuario = {"id": len(usuarios) + 1, "correo": correo, "contrasena": contrasena}
    usuarios.append(usuario)
    guardar_usuarios(usuarios)
    return True, "Registro exitoso"

def autenticar(correo, contrasena):
    usuario = buscar_por_correo(correo)
    if usuario and usuario.get("contrasena") == contrasena:
        return usuario
    return None
