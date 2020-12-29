# -*- coding: utf-8 -*-
"""
Helper functions for FastAPI app.
"""
import json
import secrets
from pathlib import Path

your_mother = Path("yo_mama.json")

# Loading our json into a python list
with your_mother.open() as r:
    mama = json.load(r)

# Creating a list of our laugh emojis
laughing = ["🤣", "😆", "😂"]


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
