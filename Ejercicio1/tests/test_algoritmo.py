import pytest
from src.algoritmo_bfs_invertido import BFSInvertido
from src.heuristica_conexion import HeuristicaConexion
from unittest.mock import Mock

@pytest.fixture
def grafo_mock():
    return {
        "D": [("C", 1), ("B", 3)],
        "C": [("A", 2)],
        "B": [("A", 5)],
        "A": []
    }

def test_buscar_ruta_optima(grafo_mock):
    heuristica_mock = Mock(spec=HeuristicaConexion)
    heuristica_mock.verificar_carga.side_effect = lambda nodo, costo: costo <= 4

    bfs = BFSInvertido(grafo_mock, heuristica_mock)
    resultado = bfs.buscar_ruta_optima("D")

    assert resultado == [("C", 1), ("A", 3), ("B", 3)]
