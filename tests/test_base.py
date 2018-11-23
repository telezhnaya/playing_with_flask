import pytest

from example.app import create_app


@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.debug = True
    app.testing = True

    with app.app_context():
        yield app


def test_app_exists(app):
    assert app.debug


def test_simple():
    assert 42 == 42
