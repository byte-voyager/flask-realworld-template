def get_token(client, username, password):
    res = client.post(
        "/api/v1/token", json={"username": username, "password": password}
    )
    assert res.status_code == 200
    assert res.json["errcode"] == 2000
    assert len(res.json["data"]["token"]) > 1
    return res.json["data"]["token"]
