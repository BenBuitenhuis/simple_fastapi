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


def test_joke_passing(the_jokes):
    """
    Ensure right jokes are given.
    """
    # GIVEN a FastAPI GET request

    # WHEN GET request to index
    response = client.get("/")

    resp = response.json()

    # THEN assert that joke is within our jokes list.
    assert resp.get("yo_mama")[:-1] in the_jokes


def test_joke_has_an_emoji(the_laughs):
    """
    Validate that an emoji is in our joke response.
    """
    # GIVEN FastAPI app

    # WHEN GET request is sent
    response = client.get("/")

    resp = response.json()

    # THEN assert that an emoji is added to the end.
    assert resp.get("yo_mama")[-1] in the_laughs
