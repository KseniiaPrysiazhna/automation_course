import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

logger = logging.getLogger("CarsAPITest")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
console_handler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


BASE_URL = "http://127.0.0.1:8080"


@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    assert response.status_code == 200, "Auth failed!"
    token = response.json()["access_token"]
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session

@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 7),
    ("brand", 10),
    ("price", 2),
    ("year", 8),
    ("engine_volume", None),
])
class TestCarsAPI:

    def test_search_cars(self, auth_session, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        response = auth_session.get(f"{BASE_URL}/cars", params=params)
        logger.info(f"Запит: /cars?{params}")
        logger.info(f"Статус код: {response.status_code}")
        logger.info(f"Відповідь: {response.json()}")

        assert response.status_code == 200
        data = response.json()

        if limit:
            assert len(data) <= limit

        if sort_by:
            values = [item[sort_by] for item in data]
            assert values == sorted(values), f"Сортування за {sort_by} некоректне"