# -*- coding: utf-8 -*-
"""
Fixtures and parametrized variables.
"""
import pytest

# Funny Yo Mama jokes not included
funny = [
    "Yo momma is so fat when she got on the scale it said, "
    "'I need your weight not your phone number.' ",
    "Yo momma's so fat and old when God said, 'Let there be light,' "
    "he asked your mother to move out of the way.",
    "Yo momma is so fat when she sat on WalMart, she lowered the prices.",
]

funny_ids = [_ for _ in funny]


@pytest.fixture(scope="function", params="funny", ids=funny_ids)
def still_funny(request):
    """
    Fixture return our jokes not in our jokes list.
    """
    return request.param
