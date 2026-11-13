class Heap:
    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        self._subir(len(self.arreglo) - 1)
        if imagen:
            self._mostrar()

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) == 1:
            raise IndexError('No se puede retirar de un heap vacío.')

        smallest = self.arreglo[1]
        last = self.arreglo.pop()
        if len(self.arreglo) > 1:
            self.arreglo[1] = last
            self._bajar(1)
        if imagen:
            self._mostrar()
        return smallest

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        last_parent = (len(self.arreglo) - 1) // 2
        for index in range(last_parent, 0, -1):
            self._bajar(index)
        if imagen:
            self._mostrar()

    def _subir(self, index):
        while index > 1:
            parent = index // 2
            if self.arreglo[parent] <= self.arreglo[index]:
                break
            self.arreglo[parent], self.arreglo[index] = (
                self.arreglo[index], self.arreglo[parent]
            )
            index = parent

    def _bajar(self, index):
        size = len(self.arreglo) - 1
        while 2 * index <= size:
            child = 2 * index
            right = child + 1
            if right <= size and self.arreglo[right] < self.arreglo[child]:
                child = right
            if self.arreglo[index] <= self.arreglo[child]:
                break
            self.arreglo[index], self.arreglo[child] = (
                self.arreglo[child], self.arreglo[index]
            )
            index = child

    def _mostrar(self):
        import matplotlib.pyplot as plt

        size = len(self.arreglo) - 1
        depth = size.bit_length() - 1 if size else 0
        figure, axis = plt.subplots(
            figsize=(max(5, 1.5 * (2 ** min(depth, 4))), max(3, 1.25 * depth + 2))
        )

        for index in range(1, size + 1):
            level = index.bit_length() - 1
            position = index - (1 << level)
            x = (position + 0.5) * 2 / (1 << level) - 1
            y = depth - level

            if index > 1:
                parent = index // 2
                parent_level = parent.bit_length() - 1
                parent_position = parent - (1 << parent_level)
                parent_x = (parent_position + 0.5) * 2 / (1 << parent_level) - 1
                parent_y = depth - parent_level
                axis.plot([parent_x, x], [parent_y, y], color='#64748b', zorder=1)

            axis.scatter([x], [y], s=1100, color='#d7eee8', edgecolor='#176b5b', zorder=2)
            axis.text(x, y, str(self.arreglo[index]), ha='center', va='center', zorder=3)

        axis.set_xlim(-1.15, 1.15)
        axis.set_ylim(-0.6, depth + 0.6)
        axis.axis('off')
        figure.tight_layout()
        plt.show()
