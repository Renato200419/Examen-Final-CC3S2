from src.heuristica_conexion import HeuristicaConexion

class BFSInvertido:
    def __init__(self, grafo, heuristica: HeuristicaConexion):
        self.grafo = grafo
        self.heuristica = heuristica

    def buscar_ruta_optima(self, destino):
        visitados = set()
        cola = [(destino, 0)]  # (nodo, costo_acumulado)
        rutas = []

        while cola:
            nodo_actual, costo = cola.pop(0)
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                if self.heuristica.verificar_carga(nodo_actual, costo):
                    rutas.append((nodo_actual, costo))
                for vecino, peso in self.grafo.get(nodo_actual, []):
                    if vecino not in visitados:
                        cola.append((vecino, costo + peso))

        return sorted(rutas, key=lambda x: x[1])  # Retorna rutas ordenadas por costo


