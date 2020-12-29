# -*- coding: utf-8 -*-
"""
The Main FastAPI app.
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.helper import laugh, yomama

app = FastAPI(
    title="Yo Mama!",
    description="A couple of random yo mama jokes.",
    version="0.1.0",
)


class Laugh(BaseModel):
    """
    Base Model for jokes.
    """

    yo_mama: str = Field(default_factory=yomama)
    laughing: str = Field(default_factory=laugh)

    class Config:
        """
        Output Schema.
        """

        schema_extra = {
            "example": {
                "yo_mama": (
                    "Yo mama so dumb she talks in a "
                    "envelope to send the voice mail.😄"
                ),
            },
        }


@app.get("/", response_model=Laugh)
async def yo_mama():
    """
    Yup!

    Yo' Mama...

    """
    return {"yo_mama": yomama() + laugh()}
