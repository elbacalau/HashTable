from typing import List, Tuple

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table: List[List[Tuple[str, str]]] = [[] for i in range(size)]
        

    def _hash(self, nif: str) -> int:
        # generar hash y encontrar el indice
        valor_hash = 0
        for pos, char in enumerate(nif):
            ascii_num = ord(char)
            valor_hash += ascii_num * (pos + 1)

        # para reducir las colisiones mutliplicamos el numero ascii del char por la posicion en la que se encuentra
        return valor_hash % self.size


    def insertar_clientes(self, nif: str, nombre: str): 
        index = self._hash(nif)
        cube: List[Tuple[str, str]] = self.table[index]

        for i, (key, value) in enumerate(cube):
            if key == nif:
                # si se encuentra actualizar el valor
                cube[i] = (nif, nombre)
                return

        # sino se encuentra el valor agregarlo
        cube.append((nif, nombre))


    def busqueda_clientes(self, nif: str):
        index = self._hash(nif)
        cube: List[Tuple[str, str]] = self.table[index]

        # si el nif coincide devolver el valor, es decir, el nombre  :)
        for key, value in cube:
            if key == nif:
                return value

        return None




resultado = HashTable(10)
resultado.insertar_clientes('J87529103', 'Supermercados Forcarei')
resultado.insertar_clientes('K98289134', 'Alimentación Lolita')
resultado.insertar_clientes('M27349102', 'Grandes Cadenas Fresquísimo')
resultado.insertar_clientes('K82709123', 'Ultramarinos Pepe')


print(resultado.busqueda_clientes('J87529103')) # => deberia devolver el nombre al que corresponde este nif
