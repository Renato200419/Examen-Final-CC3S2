from src.nodo_segment_tree import NodoSegmentTree

class SegmentTree:
    def __init__(self, arr):
        self.versiones = []  # Lista de versiones
        self.versiones.append(self._construir_arbol(arr, 0, len(arr)))

    def _construir_arbol(self, arr, start, end):
        if start == end - 1:  # Nodo hoja
            return NodoSegmentTree(start, end, arr[start])
        
        mid = (start + end) // 2
        nodo = NodoSegmentTree(start, end)
        nodo.left = self._construir_arbol(arr, start, mid)
        nodo.right = self._construir_arbol(arr, mid, end)
        nodo.value = nodo.left.value + nodo.right.value
        return nodo

    def consultar_rango(self, start, end, version):
        raiz = self.versiones[version]
        return self._consultar_rango(raiz, start, end)

    def _consultar_rango(self, nodo, start, end):
        if nodo.start >= end or nodo.end <= start:
            return 0
        if nodo.start >= start and nodo.end <= end:
            return nodo.value
        return self._consultar_rango(nodo.left, start, end) + \
               self._consultar_rango(nodo.right, start, end)
    
    def actualizar(self, index, valor, version):
        raiz_anterior = self.versiones[version]
        nueva_raiz = self._actualizar(raiz_anterior, index, valor)
        self.versiones.append(nueva_raiz)

    def _actualizar(self, nodo, index, valor):
        if nodo.start == nodo.end - 1:
            return NodoSegmentTree(nodo.start, nodo.end, valor)

        mid = (nodo.start + nodo.end) // 2
        nuevo_nodo = NodoSegmentTree(nodo.start, nodo.end)

        if index < mid:
            nuevo_nodo.left = self._actualizar(nodo.left, index, valor)
            nuevo_nodo.right = nodo.right
        else:
            nuevo_nodo.right = self._actualizar(nodo.right, index, valor)
            nuevo_nodo.left = nodo.left

        nuevo_nodo.value = nuevo_nodo.left.value + nuevo_nodo.right.value
        return nuevo_nodo