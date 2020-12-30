# -*- coding: utf-8 -*-
from src import __version__
from src.helper import laugh, laughing, the_joke, yomama


def test_version():
    """
    Test version is correct.
    """
    assert __version__ == "0.1.0"


def test_passing_yomama(the_jokes):
    """
    Passing test for yo mama function.
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

    # THEN Assert that it has one of the emojis in the our emoji list
    assert the_laugh in laughing


def test_the_joke_has_an_emoji(the_laughs):
    """
    Make sure the the_jokes functions returns joke with emoji.
    """
    # GIVEN the_jokes function

    # WHEN called
    a_joke = the_joke()

    # THEN joke contains emoji
    assert a_joke[-1] in the_laughs


def test_the_joke_has_joke_in_list(the_jokes):
    """
    Make sure the_jokes functions contains joke in list.
    """
    # GIVEN the_jokes function

    # WHEN called
    a_joke = the_joke()

    # Then joke contains joke in jokes list
    assert a_joke[:-1] in the_jokes
