# -*- coding: utf-8 -*-
import json
from pathlib import Path

__version__ = "0.1.0"

your_mother = Path("yo_mama.json").absolute()


# Loading our json into a python list
with your_mother.open() as r:
    mama = json.load(r)


# Creating a list of our laugh emojis
laughing = ["🤣", "😆", "😂"]
