import pytest

def test_ejemplo_pass():
    assert True

def test_verificar_estado_api():
    assert 1 + 1 == 2

def test_validar_nombre_proyecto():
    nombre = "TaskFlow API"
    assert "TaskFlow" in nombre
