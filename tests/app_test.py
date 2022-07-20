import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_json_data(client):
    response = client.post(
        "/detect_glare",
        json={
            "lat": 49.2699648,
            "lon": -123.1290368,
            "epoch": 1588704959.321,
            "orientation": -10.2,
        },
    )
    assert response.json["glare"] == "false"
