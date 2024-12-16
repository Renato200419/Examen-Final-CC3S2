import pytest
from src.segment_tree import SegmentTree

@pytest.fixture
def arreglo_inicial():
    return [1, 2, 3, 4, 5]

def test_creacion_arbol(arreglo_inicial):
    st = SegmentTree(arreglo_inicial)
    assert st.consultar_rango(0, 5, 0) == 15  # Suma total del arreglo

def test_actualizacion_versiones(arreglo_inicial):
    st = SegmentTree(arreglo_inicial)
    st.actualizar(2, 10, 0)  # Actualiza índice 2 a 10
    assert st.consultar_rango(0, 5, 1) == 22  # Nueva suma
    assert st.consultar_rango(0, 5, 0) == 15  # Versión original sin cambios