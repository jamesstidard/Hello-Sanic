import pytest

from hellosanic import create_app


@pytest.fixture
def app():
    return create_app()
