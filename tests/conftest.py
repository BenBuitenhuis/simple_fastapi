# -*- coding: utf-8 -*-
# tests/conftest.py
"""
Fixtures and parametrized variables.
"""
import pytest

from src import laughing, mama


@pytest.fixture(scope="function")
def the_jokes():
    """
    Returning jokes lists for tests.
    """
    return mama


@pytest.fixture(scope="function")
def the_laughs():
    """
    Return the list of laughing emojis.
    """
    return laughing
