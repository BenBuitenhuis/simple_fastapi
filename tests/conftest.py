# -*- coding: utf-8 -*-
"""
Fixtures and parametrized variables.
"""
import json
from pathlib import Path

import pytest

your_mother = Path("../yo_mama.json")

with your_mother.open() as r:
    """
    Reading JSON file of "Yo Mama" jokes.
    """
    jokes = json.load(r)


@pytest.fixture(scope="function", params=jokes)
def the_jokes(request):
    """
    Returning jokes lists for tests.
    """
    return request.params
