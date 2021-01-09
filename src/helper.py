# -*- coding: utf-8 -*-
# src/helper.py
"""
Helper functions for FastAPI app.
"""
import secrets

from src import laughing, mama


def yomama():
    """
    Function that returns a random "Yo Mama!" joke.
    """
    return secrets.choice(mama)


def laugh():
    """
    Function that returns a random laughing emoji.
    """
    return secrets.choice(laughing)


def the_joke():
    """
    Combining both joke and emojis into one function.
    """
    return yomama() + laugh()
