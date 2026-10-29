import pytest
from src.inventario import detectar_sobrestock, porcentaje_inventario


def test_hay_sobrestock():
    assert detectar_sobrestock(120, 100) is True


def test_no_hay_sobrestock_en_el_limite():
    # justo en el maximo todavia no es sobrestock
    assert detectar_sobrestock(100, 100) is False


def test_sobrestock_maximo_invalido():
    with pytest.raises(ValueError):
        detectar_sobrestock(50, 0)


def test_porcentaje_inventario():
    assert porcentaje_inventario(45, 60) == 75.0


def test_porcentaje_stock_negativo():
    with pytest.raises(ValueError):
        porcentaje_inventario(-1, 60)
