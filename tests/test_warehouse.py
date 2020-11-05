from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '')
from main import app


client = TestClient(app)


def test_create_category():
    json = {
        "name": "Колготы"
    }
    response = client.post("/category/", json=json)
    assert response.status_code == 200
    assert response.json() == {
        "name": "Колготы",
        "id": 1
    }

def test_create_product():
    json = {
        "name": "Милана+",
        "sku": "COL23RU10",
        "balance": 5,
        "category_id": 1
    }
    response = client.post("/product/", json=json)
    assert response.status_code == 200
    assert response.json() == {
        "name": "Милана+",
        "sku": "COL23RU10",
        "balance": 5,
        "id": 1,
        "category_id": 1,
        "reserve": 0
    }

def test_get_product_by_id():
    response = client.get("/product/1/")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Милана+",
        "sku": "COL23RU10",
        "balance": 5,
        "id": 1,
        "category_id": 1,
        "reserve": 0
    }

def test_update_product_by_id():
    json = {
        "balance" : 1
    }
    response = client.put("/product/1/", json=json)
    assert response.status_code == 200
    assert response.json() == {
        "name": "Милана+",
        "sku": "COL23RU10",
        "balance": 1,
        "id": 1,
        "category_id": 1,
        "reserve": 0
    }

def test_get_product_by_sku():
    response = client.get("/product/?sku=COL23RU10")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Милана+",
        "sku": "COL23RU10",
        "balance": 1,
        "id": 1,
        "category_id": 1,
        "reserve": 0
    }