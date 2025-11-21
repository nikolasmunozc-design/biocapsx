import json
import os

DATA_DIR = "data"
USUARIOS_FILE = os.path.join(DATA_DIR, "usuarios.json")
PRODUCTOS_FILE = os.path.join(DATA_DIR, "productos.json")
COMPRAS_FILE = os.path.join(DATA_DIR, "compras.json")

def asegurar_directorio():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def leer_json(ruta, valor_por_defecto):
    asegurar_directorio()
    if not os.path.exists(ruta):
        escribir_json(ruta, valor_por_defecto)
        return valor_por_defecto
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        escribir_json(ruta, valor_por_defecto)
        return valor_por_defecto

def escribir_json(ruta, datos):
    asegurar_directorio()
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

def cargar_usuarios():
    return leer_json(USUARIOS_FILE, [])

def guardar_usuarios(usuarios):
    escribir_json(USUARIOS_FILE, usuarios)

def cargar_productos():
    return leer_json(PRODUCTOS_FILE, productos_por_defecto())

def guardar_productos(productos):
    escribir_json(PRODUCTOS_FILE, productos)

def cargar_compras():
    return leer_json(COMPRAS_FILE, [])

def guardar_compras(compras):
    escribir_json(COMPRAS_FILE, compras)

def productos_por_defecto():
    return [
        {"id": 1, "nombre": "Cápsula Estándar", "tipo": "capsula", "precio": 7000},
        {"id": 2, "nombre": "Cápsula Sensor", "tipo": "capsula_sensor", "precio": 18000},
        {"id": 3, "nombre": "Kit Inicio (5 cápsulas)", "tipo": "kit", "precio": 30000}
    ]
