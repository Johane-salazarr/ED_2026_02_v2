class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        # Agregar el nuevo valor al final del arreglo
        self.arreglo.append(valor)

        # Almacenar la posición donde se inserta el valor 
        i = len(self.arreglo) - 1
       
        # Mientras no este en la posición del root
        while i > 1:
          # Calcular posición del padre
            padre = i // 2
          
          # Sí el padre es menor o igual que el hijo, 
          # el heap está ordenado de forma correcta
            if self.arreglo[padre] <= self.arreglo[i]:
                break
          # Sí el hijo es menor que su padre, intercambia los valores
            self.arreglo[i], self.arreglo[padre] = (
                self.arreglo[padre],
                self.arreglo[i]
            )
          # Seguir comprobando la posición del padre
            i = padre

    def remove_smallest(self):
        # Sí el heap esta vacio no hay nada que que eliminar
        if len(self.arreglo) == 1:
            return None
        # El elemento más pequeño siempre esta en la posición 1
        menor = self.arreglo[1]

        # Sacar el último elemento del arreglo
        ultimo = self.arreglo.pop()
        # Sí después de quitarlo no quedan valores, se retorna el valor menor
        if len(self.arreglo) == 1:
            return menor
        # Ponemos el último elemento del arreglo
        self.arreglo[1] = ultimo

        # Revisar desde la raiz
        i = 1
        # Mientras que el elemento esté en su posición correcta
        while True:
            # Posición del hijo izquierdo
            izquierdo = 2 * i
            # Posición del hijo derecho
            derecho = 2 * i + 1
            # Suponemos que el elemento actual es el menor de los tres elementos
            menor_hijo = i

            # Si existe el hijo izquierdo y es menor que el actual, 
            # almacenamos su posición
            if izquierdo < len(self.arreglo):
                if self.arreglo[izquierdo] < self.arreglo[menor_hijo]:
                    menor_hijo = izquierdo

            # Si existe el hijo derecho y es menor que el actual
            # almacenamos su posición
            if derecho < len(self.arreglo):
                if self.arreglo[derecho] < self.arreglo[menor_hijo]:
                    menor_hijo = derecho

            # Si el elemento actual ya esta en la posición correcta ...
            if menor_hijo == i:
                break
           
            # Intercamnbiamos el elemento con su hijo menor
            self.arreglo[i], self.arreglo[menor_hijo] = (
                self.arreglo[menor_hijo],
                self.arreglo[i]
            ) 
            # Continuamos desde la posición a la que bajamos

            i = menor_hijo

        # Retorna el elemento que eliminamos  
        return menor


    def build_heap(self, lista):
        pass
