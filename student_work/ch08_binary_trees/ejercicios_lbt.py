from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


def es_completo(T):
    """Retorna True si el LinkedBinaryTree T es completo."""
    # Si el arbol está vacío, se considera completo
    if len(T) == 0:
        return True

    # Crear una cola que almacena los nodos
    # para recorrer el arbol por niveles
    cola = [T.root()]

    # Variable que indica si ya encontramos un hueco
    hueco = False

    # Recorremos los nodos del arbol por niveles
    while cola:

        # Sacar el primer nodo de la cola
        nodo = cola.pop(0)

        # Obtener el hijo izquierdo y derecho
        izquierdo = T.left(nodo)
        derecho = T.right(nodo)

        # Si ya encontramos un hueco y este nodo tiene
        # algun hijo, el arbol no es completo
        if hueco and (izquierdo is not None or derecho is not None):
            return False

        # Si no tiene hijo izquierdo
        if izquierdo is None:
            # Encontramos un hueco
            hueco = True
        else:
            # Agregamos el hijo izquierdo a la cola
            cola.append(izquierdo)

        # Si no tiene hijo derecho
        if derecho is None:
            # Encontramos un hueco
            hueco = True
        else:
            # Si ya habia un hueco, significa que este
            # hijo aparece despues de un espacio vacio
            if hueco:
                return False

            # Agregamos el hijo derecho a la cola
            cola.append(derecho)

    # Si termina el recorrido sin encontrar un problema
    return True



def camino(T, p, q):
    """Retorna el camino de p a q como string: 'H -> D -> B -> E'."""

    # Creamos una lista que comienza con p
    # Se almacenara el camino desde p hasta la raiz
    camino1 = [p]

    # Almacena temporalmente el nodo p
    actual = p

    # Mientras que el nodo actual tenga un padre,
    # seguimos subiendo de nivel hacia la raiz
    while T.parent(actual) is not None:
        # Padre del nodo actual
        actual = T.parent(actual)

        # Agregar el padre a la lista del camino
        camino1.append(actual)

    # Creamos una lista adicional con q
    # Se almacena el camino desde q hasta la raiz
    camino2 = [q]
    actual = q

    # Mientras el nodo actual tenga un padre,
    # seguimos subiendo de nivel hacia la raiz
    while T.parent(actual) is not None:
        # Padre del nodo actual
        actual = T.parent(actual)

        # Agregar el padre a la lista del camino
        camino2.append(actual)

    # Recorremos todos los nodos del camino desde p hasta la raiz
    for i in range(len(camino1)):

        # Recorremos todos los nodos del camino desde q hasta la raiz
        for j in range(len(camino2)):

            # Si encontramos un nodo que pertenece a ambos caminos,
            # este sera el ancestro comun mas bajo
            if camino1[i] == camino2[j]:

                # Tomamos desde p hasta el ancestro comun
                ruta = camino1[:i + 1]

                # Si el ancestro comun no es q,
                # agregamos la parte restante del camino
                if j > 0:
                    ruta += camino2[j - 1::-1]

                # Convertimos los nodos en sus elementos
                # y los unimos utilizando " -> "
                return " -> ".join(str(nodo.element()) for nodo in ruta)

    # Si no se encuentra un ancestro comun
    return ""




if __name__ == "__main__":
    # tus pruebas (opcional)
    pass
