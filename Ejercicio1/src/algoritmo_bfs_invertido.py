import heapq
from src.heuristica_conexion import HeuristicaConexion

class BFSInvertido:
    def __init__(self, grafo, heuristica: HeuristicaConexion):
        self.grafo = grafo
        self.heuristica = heuristica

    def buscar_ruta_optima(self, destino):
        visitados = {}  # Diccionario para almacenar el menor costo a cada nodo
        cola = []
        heapq.heappush(cola, (0, destino))  # (costo acumulado, nodo)
        rutas = []

        while cola:
            costo, nodo_actual = heapq.heappop(cola)

            # Si el nodo ya fue visitado con un menor costo, se ignora
            if nodo_actual in visitados and visitados[nodo_actual] <= costo:
                continue

            visitados[nodo_actual] = costo

            # Evitar incluir el nodo destino en los resultados
            if nodo_actual != destino and self.heuristica.verificar_carga(nodo_actual, costo):
                rutas.append((nodo_actual, costo))

            # Agrega los vecinos a la cola
            for vecino, peso in self.grafo.get(nodo_actual, []):
                heapq.heappush(cola, (costo + peso, vecino))

        return sorted(rutas, key=lambda x: x[1])  # Ordena por costo acumulado
