# -*- coding: utf-8 -*-
from src import __version__
from src.helper import laugh, laughing, yomama


def test_version():
    """
    Test version is correct.
    """
    assert __version__ == "0.1.0"


def test_passing_yomama(the_jokes):
    """
    Passing test for you mama.
    """
    # GIVEN yomama function
    mama = yomama

    # WHEN called
    joke = mama()

    # THEN a random joke is given that's in our jokes list
    assert joke in the_jokes


def test_laughing():
    """
    Testing laughing emoji function.
    """
    # GIVEN laugh function

    # WHEN called
    the_laugh = laugh()

    # Assert that it has one of the emojis in the list
    assert the_laugh in laughing
