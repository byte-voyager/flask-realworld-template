import pytest

from app import create_app

app = create_app("config.current_config")
app.config.update({"TESTING": True})


@pytest.fixture(scope="session")
def client():
    print("1" * 40)
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client
