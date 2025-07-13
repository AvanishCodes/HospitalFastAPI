from fastapi.testclient import TestClient
from hospital import app

client = TestClient(app)


def test_create_hospital():
    payload = {
        "name": "Test Hospital",
        "address": "123 Test St",
        "phone": "1234567890",
        "email": "test@hospital.com"
    }
    response = client.post("/api/v1/hospital", json=payload)
    assert response.status_code == 200 or response.status_code == 201
    data = response.json()
    assert data["status"] == "success"
    assert data["hospital"]["name"] == payload["name"]
    assert data["hospital"]["address"] == payload["address"]
    assert data["hospital"]["phone"] == payload["phone"]
    assert data["hospital"]["email"] == payload["email"]
    return data["hospital"]["id"]


def test_get_all_hospitals():
    response = client.get("/api/v1/hospital")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["hospitals"], list)


def test_get_hospital_by_id():
    # First, create a hospital
    payload = {
        "name": "Test Hospital 2",
        "address": "456 Test Ave",
        "phone": "9876543210",
        "email": "test2@hospital.com"
    }
    create_resp = client.post("/api/v1/hospital", json=payload)
    assert create_resp.status_code == 200 or create_resp.status_code == 201
    hospital_id = create_resp.json()["hospital"]["id"]

    # Now, get by id
    response = client.get(f"/api/v1/hospital/{hospital_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["hospital"]["id"] == hospital_id


def test_update_hospital():
    # First, create a hospital
    payload = {
        "name": "Test Hospital 3",
        "address": "789 Test Blvd",
        "phone": "5555555555",
        "email": "test3@hospital.com"
    }
    create_resp = client.post("/api/v1/hospital", json=payload)
    assert create_resp.status_code == 200 or create_resp.status_code == 201
    hospital_id = create_resp.json()["hospital"]["id"]

    # Update
    update_payload = {
        "name": "Updated Hospital 3",
        "address": "789 Updated Blvd",
        "phone": "1111111111",
        "email": "updated3@hospital.com"
    }
    response = client.put(f"/api/v1/hospital/{hospital_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["hospital"]["name"] == update_payload["name"]


def test_delete_hospital():
    # First, create a hospital
    payload = {
        "name": "Test Hospital 4",
        "address": "101 Test Rd",
        "phone": "2222222222",
        "email": "test4@hospital.com"
    }
    create_resp = client.post("/api/v1/hospital", json=payload)
    assert create_resp.status_code == 200 or create_resp.status_code == 201
    hospital_id = create_resp.json()["hospital"]["id"]

    # Delete
    response = client.delete(f"/api/v1/hospital/{hospital_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"

    # Confirm deletion
    get_resp = client.get(f"/api/v1/hospital/{hospital_id}")
    assert get_resp.status_code == 404
