# -*- coding: utf-8 -*-
"""
Helper functions for FastAPI app.
"""
import json
import secrets

with open("yo_mama.json") as r:
    mama = json.load(r)


def yomama():
    """
    Function that returns a random "Yo Mama!" joke.
    """
    return secrets.choice(mama)
