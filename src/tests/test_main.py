from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add():
    res = client.get("/add?a=3&b=5")
    assert res.status_code == 200
    assert res.json() == {"result": 8}

def test_subtract():
    res = client.get("/subtract?a=10&b=4")
    assert res.status_code == 200
    assert res.json() == {"result": 6}

def test_multiply():
    res = client.get("/multiply?a=7&b=6")
    assert res.status_code == 200
    assert res.json() == {"result": 42}

def test_divide():
    res = client.get("/divide?a=20&b=5")
    assert res.status_code == 200
    assert res.json() == {"result": 4}

def test_divide_by_zero():
    res = client.get("/divide?a=10&b=0")
    assert res.status_code == 200
    assert res.json() == {"error": "Cannot divide by zero"}

def test_power():
    res = client.get("/power?a=2&b=3")
    assert res.status_code == 200
    assert res.json() == {"result": 8}

def test_modulo():
    res = client.get("/modulo?a=10&b=3")
    assert res.status_code == 200
    assert res.json() == {"result": 1}

def test_modulo_by_zero():
    res = client.get("/modulo?a=10&b=0")
    assert res.status_code == 200
    assert res.json() == {"error": "Cannot modulo by zero"}

def test_average():
    res = client.get("/average?a=10&b=20")
    assert res.status_code == 200
    assert res.json() == {"result": 15}
