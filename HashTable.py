class person:
    def __init__(self, name: str, phone: str, address: str):
        self.name = name
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Address: {self.address}"

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            bucket_str = ", ".join(f"({k}: {v})" for k, v in bucket)
            result.append(f"Index {i}: [{bucket_str}]")
        return "\n".join(result)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una tabla hash con tamaño 5
    hash_table = HashTable(size=5)

    # Crear instancias de la clase person
    person1 = person("Alice", "123-456-7890", "123 Main St")
    person2 = person("Bob", "987-654-3210", "456 Elm St")
    person3 = person("Charlie", "555-555-5555", "789 Oak St")

    # Insertar personas en la tabla hash
    print("Insertando personas en la tabla hash...")
    hash_table.insert(person1.name, person1)
    hash_table.insert(person2.name, person2)
    hash_table.insert(person3.name, person3)

    # Obtener una persona por su nombre
    print("\nObteniendo a Bob:")
    print(hash_table.get("Bob"))

    # Eliminar una persona
    print("\nEliminando a Alice:")
    hash_table.remove("Alice")
    print("Estado de la tabla después de eliminar a Alice:")
    print(hash_table)

    # Intentar obtener a Alice después de eliminarla
    print("\nIntentando obtener a Alice después de eliminarla:")
    result = hash_table.get("Alice")
    print("Resultado:", result if result else "No encontrado")

    # Mostrar el estado completo de la tabla hash
    print("\nEstado completo de la tabla hash:")
    print(hash_table)