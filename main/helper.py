# -*- coding: utf-8 -*-
"""
Helper functions for FastAPI app.
"""
import json
import secrets

# Loading our json into a python list
with open("yo_mama.json") as r:
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
