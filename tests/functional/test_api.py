# -*- coding: utf-8 -*-
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_joke_200():
    """
    Ensure joke is given.
    """
    # GIVEN FastAPI app

    # WHEN GET request to root is given
    response = client.get("/")

    # THEN 200 is returned
    assert response.status_code == 200


def test_joke_passing():
    """
    Ensure right jokes are given.
    """
