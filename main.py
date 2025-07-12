import random
import sqlite3
from typing import Union
from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()

answer_list = ["YES", "NO", "MAYBE"]

@app.get("/8ball")
def get_answer():
    ## TODO: Random answer
    return { "answer": "Okay inw za"}

@app.post("/8ball")
def add_answer(new_answer: str):
    ## TODO: Update list of answer with new_answer
    return answer_list
