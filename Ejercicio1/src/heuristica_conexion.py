class HeuristicaConexion:
    def __init__(self, threshold):
        self.threshold = threshold  # Umbral de carga permitido

    def verificar_carga(self, nodo, costo):
        # Simula un cálculo de carga en función del costo
        if costo > self.threshold:
            return False
        return True
