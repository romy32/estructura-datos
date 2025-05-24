class Producto:
    def __init__(self, nombre, peso, categoria):
        self.nombre = nombre
        self.peso = peso
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} ({self.categoria}, {self.peso} kg)"

class ProductoDevuelto:
    def __init__(self, producto, razon):
        self.producto = producto
        self.razon = razon

    def __str__(self):
        return f"{self.producto} - Razón: {self.razon}"

class ColaEmpaque:
    def __init__(self):
        self.cola = []

    def encolar(self, producto):
        self.cola.append(producto)
        # Ordenamos por peso (opcional, comentar si no quieres)
        # self.ordenar_por_peso()

    def desencolar(self):
        if self.cola:
            return self.cola.pop(0)
        return None

    def eliminar_producto(self, nombre):
        for i, prod in enumerate(self.cola):
            if prod.nombre == nombre:
                return self.cola.pop(i)
        return None

    def obtener_productos(self):
        return self.cola

    def ordenar_por_peso(self):
        self.cola.sort(key=lambda p: p.peso)
