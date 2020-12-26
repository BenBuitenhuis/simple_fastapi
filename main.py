"""
The Main FastAPI app
"""
from fastapi import FastAPI


app = FastAPI(
    title="Yo Mama!",
    description="A couple of random yo mama jokes.",
    version="0.1.0"
)


@app.get()
def yo_mama():
    """Yup! Yo' Mama..."""
    pass
