class Cliente:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.pedidos = []

    def agregar_pedido(self, productos):
        self.pedidos.append(productos)

    def obtener_historial(self):
        return self.pedidos

    def sugerir_categorias(self):
        from collections import Counter
        categorias = []
        for pedido in self.pedidos:
            for producto in pedido:
                categorias.append(producto.categoria)
        contador = Counter(categorias)
        if contador:
            max_cate = contador.most_common(1)[0][0]
            return [max_cate]
        return []
