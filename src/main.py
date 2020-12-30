# -*- coding: utf-8 -*-
# src/main.py
"""
The Main FastAPI app.
"""
from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.helper import the_joke

app = FastAPI(
    title="Yo Mama!",
    description="A couple of random yo mama jokes.",
    version="0.1.0",
    docs_url="/",
)


class Laugh(BaseModel):
    """
    Schema for our Yo' Mama!

    jokes.

    """

    yo_mama: str = Field(default_factory=the_joke)

    class Config:
        """
        Output Schema.
        """

        schema_extra = {
            "example": {
                "yo_mama": (
                    "Yo mama so dumb she talks in an "
                    "envelope to send the voice mail.😄"
                ),
            },
        }


@app.get("/yo_mama", response_model=Laugh)
async def yo_mama():
    """
    Yup!

    Yo' Mama!!!

    """
    return {"yo_mama": the_joke()}
