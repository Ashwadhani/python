import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# ---------- Addition ----------
def test_add():
    response = client.get("/add", params={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8.0}

# ---------- Subtraction ----------
def test_subtract():
    response = client.get("/subtract", params={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6.0}

# ---------- Multiplication ----------
def test_multiply():
    response = client.get("/multiply", params={"a": 2, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 14.0}

# ---------- Division ----------
def test_divide():
    response = client.get("/divide", params={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_divide_by_zero():
    response = client.get("/divide", params={"a": 10, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"error": "Cannot divide by zero"}

# ---------- Power ----------
def test_power():
    response = client.get("/power", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8.0}

# ---------- Modulo ----------
def test_modulo():
    response = client.get("/modulo", params={"a": 10, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 1.0}

def test_modulo_by_zero():
    response = client.get("/modulo", params={"a": 10, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"error": "Cannot modulo by zero"}

# ---------- Average ----------
def test_average():
    response = client.get("/average", params={"a": 4, "b": 6})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}
