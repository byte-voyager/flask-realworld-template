from tests.api.utils import get_token


def test_post_users(client):
    res = client.post(
        "/api/v1/users", json={"username": "NO-USER", "password": "123456"}
    )
    assert res.status_code == 200


def test_get_users(client):
    res = client.get("/api/v1/users?page=1&size=2")
    assert res.status_code == 200
    res = client.get("/api/v1/users?page=0&size=2")
    assert res.status_code == 200
    res = client.get("/api/v1/users?page=-1&size=2")
    assert res.status_code == 200
    res = client.get("/api/v1/users?page=&size=2")
    assert res.status_code == 200
    res = client.get("/api/v1/users?page=&size=")
    assert res.status_code == 200


def test_delete_users(client):
    test_post_users(client)
    token = get_token(client, "NO-USER", "123456")
    res = client.get(
        "/api/v1/users?page=1&size=1&username=NO-USER",
        headers={"Authorization": "Bearer " + token},
    )
    assert res.status_code == 200
    assert res.json["data"]["total_count"] > 0
    assert "password" not in res.json["data"]["list"][0].keys()
    user_id = res.json["data"]["list"][0]["id"]

    assert user_id is not None

    res = client.delete(
        "/api/v1/users/" + str(user_id), headers={"Authorization": "Bearer " + token}
    )
    assert res.json["errcode"] == 2000

    res = client.get(
        "/api/v1/users?page=1&size=1&username=NO-USER",
        headers={"Authorization": "Bearer " + token},
    )
    assert res.json["data"]["total_count"] == 0
