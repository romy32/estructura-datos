import pandas as pd

# 🔹 Cargar el archivo CSV
# Asegúrate de que el archivo esté en la misma carpeta que este script
df = pd.read_csv("excel/Hospital.csv", 
                 encoding='latin-1', sep=';')

# 🔹 Limpiar el campo NIT: quitar comas y convertir a entero
df["Número NIT"] = df["Número NIT"].str.replace(",", "").str.replace('"', "").astype(int)

# 🔹 Clase que representa un nodo del árbol binario
class NodoHospital:
    def __init__(self, nit, razon_social, sede, municipio):
        self.nit = nit
        self.razon_social = razon_social
        self.sede = sede
        self.municipio = municipio
        self.izquierda = None
        self.derecha = None

# 🔹 Clase del Árbol Binario de Búsqueda (BST)
class ArbolHospitales:
    def __init__(self):
        self.raiz = None

    # Inserta un nuevo hospital en el árbol basado en su NIT
    def insertar(self, nodo, nit, razon_social, sede, municipio):
        if nodo is None:
            return NodoHospital(nit, razon_social, sede, municipio)
        if nit < nodo.nit:
            nodo.izquierda = self.insertar(nodo.izquierda, nit, razon_social, sede, municipio)
        else:
            nodo.derecha = self.insertar(nodo.derecha, nit, razon_social, sede, municipio)
        return nodo

    # Recorrido inorder (NITs en orden ascendente)
    def recorrido_inorder(self, nodo):
        if nodo:
            self.recorrido_inorder(nodo.izquierda)
            print(f"NIT: {nodo.nit} | Org: {nodo.razon_social} | "
                  f"Sede: {nodo.sede} | Municipio: {nodo.municipio}")
            self.recorrido_inorder(nodo.derecha)

# 🔹 Crear el árbol y agregar todos los hospitales
arbol = ArbolHospitales()

for _, row in df.iterrows():
    arbol.raiz = arbol.insertar(
        arbol.raiz,
        row["Número NIT"],
        row["Razón Social Organización"],
        row["Nombre Sede"],
        row["Nombre Municipio"]
    )

# 🔹 Mostrar todos los hospitales en orden por NIT
print("\n📋 Lista de hospitales (ordenada por NIT):")
arbol.recorrido_inorder(arbol.raiz)

# 🔹 Buscar un hospital por su NIT
def buscar_hospital(nodo, nit_buscado):
    if nodo is None:
        return "🚫 Hospital no encontrado"
    if nodo.nit == nit_buscado:
        return f"✅ Organización: {nodo.razon_social}\n   Sede: {nodo.sede}\n   Municipio: {nodo.municipio}"
    elif nit_buscado < nodo.nit:
        return buscar_hospital(nodo.izquierda, nit_buscado)
    else:
        return buscar_hospital(nodo.derecha, nit_buscado)

# 🔍 Ejemplo: buscar hospital por NIT
print("\n🔎 Buscando hospital con NIT 890980643...")
print(buscar_hospital(arbol.raiz, 890980643))
