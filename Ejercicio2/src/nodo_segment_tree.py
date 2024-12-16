class NodoSegmentTree:
    def __init__(self, start, end, value=0):
        self.start = start  # Rango [start, end)
        self.end = end
        self.value = value  # Valor agregado (suma, max, etc.)
        self.left = None  # Referencia al hijo izquierdo
        self.right = None  # Referencia al hijo derecho