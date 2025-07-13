"""Minimal FastAPI backend used in the docs and tests."""

from fastapi import FastAPI
from pydantic import BaseModel

from .projects import PROJECTS, Project

app = FastAPI()


class Profile(BaseModel):
    uid: str
    display_name: str


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a short welcome message."""
    return {"message": "gpt-fusion backend"}


@app.get("/profile/{uid}", response_model=Profile)
def get_profile(uid: str):
    return Profile(uid=uid, display_name=f"User {uid}")


@app.get("/projects", response_model=list[Project])
def list_projects() -> list[Project]:
    """Return the sample projects bundled with the repo."""
    return PROJECTS
