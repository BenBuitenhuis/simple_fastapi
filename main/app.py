# -*- coding: utf-8 -*-
"""
The Main FastAPI app.
"""
from fastapi import FastAPI

from main.helper import laugh, yomama

app = FastAPI(
    title="Yo Mama!",
    description="A couple of random yo mama jokes.",
    version="0.1.0",
)


@app.get("/")
async def yo_mama():
    """
    Yup!

    Yo' Mama...

    """
    return {"yo_mama": yomama() + laugh()}
