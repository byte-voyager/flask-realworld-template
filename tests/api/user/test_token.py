def test_1(client):
    res = client.post(
        "/api/v1/token", json={"username": "NO-USER", "password": "123456"}
    )
    assert res.status_code == 200
