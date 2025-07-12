from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Profile(BaseModel):
    uid: str
    display_name: str


@app.get("/profile/{uid}", response_model=Profile)
def get_profile(uid: str):
    return Profile(uid=uid, display_name=f"User {uid}")
