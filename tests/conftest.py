# -*- coding: utf-8 -*-
# tests/conftest.py
"""
Fixtures and parametrized variables.
"""
import json
from pathlib import Path

import pytest

from src.helper import laughing

your_mother = Path("yo_mama.json").absolute()

with your_mother.open() as r:
    """
    Reading in JSON file of "Yo Mama" jokes and converting to Python
    list.
    """
    jokes = json.load(r)


@pytest.fixture(scope="function")
def the_jokes():
    """
    Returning jokes lists for tests.
    """
    return jokes


@pytest.fixture(scope="function")
def the_laughs():
    """
    Return the list of laughing emojis.
    """
    return laughing
