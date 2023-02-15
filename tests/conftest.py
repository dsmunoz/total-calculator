from app import app
import pytest

@pytest.fixture()
def client():
    app.debug = True
    with app.test_client() as client:
        yield client
