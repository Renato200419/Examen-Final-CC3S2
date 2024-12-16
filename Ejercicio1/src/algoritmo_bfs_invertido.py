import heapq
from src.heuristica_conexion import HeuristicaConexion

class BFSInvertido:
    def __init__(self, grafo, heuristica: HeuristicaConexion):
        self.grafo = grafo
        self.heuristica = heuristica

    def buscar_ruta_optima(self, destino):
        visitados = set()  # Conjunto para marcar nodos visitados
        cola = [(0, destino)]  # Min-heap: (costo_acumulado, nodo_actual)
        resultado = []

        while cola:
            costo, nodo_actual = heapq.heappop(cola)

            # Si el nodo ya fue visitado con menor costo, lo ignoramos
            if nodo_actual in visitados:
                continue

            # Marcar el nodo como visitado
            visitados.add(nodo_actual)

            # Ignorar el nodo destino en el resultado
            if nodo_actual != destino:
                resultado.append((nodo_actual, costo))

            # Explorar vecinos hacia atrás en el grafo
            for vecino, peso in self.grafo.get(nodo_actual, []):
                nuevo_costo = costo + peso
                if vecino not in visitados and self.heuristica.verificar_carga(vecino, nuevo_costo):
                    heapq.heappush(cola, (nuevo_costo, vecino))

        # Ordenar resultados por costo acumulado
        return sorted(resultado, key=lambda x: x[1])
