from app import schemas
from jose import jwt
from app.config import settings
import pytest



# def test_root(client):
#     response = client.get("/")
#     print(response.json().get("message"))
#     assert response.json().get("message") == "Hello world!"


def test_create_user(client):
    res = client.post("/users/", json={"email": "hello123@gmail.com", "password": "1234"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "hello123@gmail.com"


def test_login_user(test_user, client):
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code",
                    [("sss@gmail.com", "12dsfcf", 403),
                     ("hello123@gmail.com", None, 422),
                     (None, "1234", 422)])
def test_incorrect_login(test_user, client, email, password, status_code):
    res = client.post("/login", data={"username": email, "password": password})

    assert res.status_code == status_code
    # assert res.json().get('detail') == "Invalid Credentials"
