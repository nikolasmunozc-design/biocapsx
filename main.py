import sys
from datos import cargar_productos, cargar_compras, guardar_compras
from usuario import registrar, autenticar, buscar_por_correo
from datos import guardar_productos

def mostrar_menu_principal():
    print("="*40)
    print("BIENCAPSX - CONSOLA")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Ver productos (sin iniciar sesión)")
    print("4. Salir")
    print("="*40)

def menu_usuario(usuario):
    print("-"*40)
    print("Usuario:", usuario.get("correo"))
    print("1. Ver productos")
    print("2. Simular compra")
    print("3. Ver historial de compras")
    print("4. Cerrar sesión")
    print("-"*40)

def listar_productos():
    productos = cargar_productos()
    print("\nProductos disponibles:")
    for p in productos:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']}")
    print("")

def ver_detalle_producto():
    productos = cargar_productos()
    try:
        pid = int(input("Ingrese ID del producto: ").strip())
    except:
        print("ID inválido")
        return
    for p in productos:
        if p["id"] == pid:
            print("-"*30)
            print("Nombre:", p["nombre"])
            print("Tipo:", p.get("tipo", ""))
            print("Precio: $", p["precio"])
            print("-"*30)
            return
    print("Producto no encontrado")

def simular_compra(usuario):
    productos = cargar_productos()
    listar_productos()
    try:
        pid = int(input("Ingrese ID del producto a comprar: ").strip())
    except:
        print("ID inválido")
        return
    producto = None
    for p in productos:
        if p["id"] == pid:
            producto = p
            break
    if not producto:
        print("Producto no encontrado")
        return
    try:
        cantidad = int(input("Ingrese cantidad: ").strip())
        if cantidad <= 0:
            print("Cantidad debe ser mayor que 0")
            return
    except:
        print("Cantidad inválida")
        return
    compras = cargar_compras()
    total = producto["precio"] * cantidad
    registro = {
        "compra_id": len(compras) + 1,
        "usuario_id": usuario["id"],
        "usuario_correo": usuario["correo"],
        "producto_id": producto["id"],
        "producto_nombre": producto["nombre"],
        "cantidad": cantidad,
        "total": total
    }
    compras.append(registro)
    guardar_compras(compras)
    print(f"Compra simulada. Total: ${total}")

def ver_historial(usuario):
    compras = cargar_compras()
    filas = [c for c in compras if c["usuario_id"] == usuario["id"]]
    if not filas:
        print("No hay compras registradas")
        return
    for c in filas:
        print("-"*30)
        print("Compra ID:", c["compra_id"])
        print("Producto:", c["producto_nombre"])
        print("Cantidad:", c["cantidad"])
        print("Total: $", c["total"])

def opcion_registrar():
    correo = input("Correo: ").strip()
    contrasena = input("Contraseña: ").strip()
    ok, msg = registrar(correo, contrasena)
    print(msg)

def opcion_iniciar_sesion():
    correo = input("Correo: ").strip()
    contrasena = input("Contraseña: ").strip()
    user = autenticar(correo, contrasena)
    if user:
        print("Inicio de sesión exitoso")
        return user
    print("Credenciales incorrectas")
    return None

def main():
    # asegurar que existan productos por defecto
    productos = cargar_productos()
    if not productos:
        guardar_productos([])
    usuario_actual = None
    while True:
        if not usuario_actual:
            mostrar_menu_principal()
            opt = input("Seleccione una opción: ").strip()
            if opt == "1":
                opcion_registrar()
            elif opt == "2":
                usuario_actual = opcion_iniciar_sesion()
            elif opt == "3":
                listar_productos()
            elif opt == "4":
                print("Saliendo...")
                sys.exit(0)
            else:
                print("Opción inválida")
        else:
            menu_usuario(usuario_actual)
            opt = input("Seleccione una opción: ").strip()
            if opt == "1":
                listar_productos()
                ver_detalle_producto()
            elif opt == "2":
                simular_compra(usuario_actual)
            elif opt == "3":
                ver_historial(usuario_actual)
            elif opt == "4":
                usuario_actual = None
            else:
                print("Opción inválida")

if __name__ == "__main__":
    main()