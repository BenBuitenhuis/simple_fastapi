# -*- coding: utf-8 -*-
import json

from main import __version__
from main.helper import laugh, laughing, yomama

with open("yo_mama.json") as read:
    """
    Getting joke list.
    """
    jokes = json.load(read)


def test_version():
    """
    Test version is correct.
    """
    assert __version__ == "0.1.0"


def test_passing_yomama():
    """
    Passing test for you mama.
    """
    # GIVEN yomama function
    mama = yomama

    # WHEN called
    the_joke = mama()

    # THEN a random joke is given that's in our jokes list
    assert the_joke in jokes


def test_laughing():
    """
    Testing laughing emoji function.
    """
    # GIVEN laugh function

    # WHEN called
    the_laugh = laugh()

    # Assert that it has one of the emojis in the list
    assert the_laugh in laughing
