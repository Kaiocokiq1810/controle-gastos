import sys
import os
from src.app import adicionar_gasto, total_gastos


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_adicionar_gasto():
    adicionar_gasto("teste", 10)
    assert total_gastos() == 10


def test_valor_negativo():
    try:
        adicionar_gasto("erro", -5)
        assert False
    except ValueError:
        assert True


def test_total():
    adicionar_gasto("a", 10)
    adicionar_gasto("b", 20)
    assert total_gastos() >= 30
