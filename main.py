import random
import sqlite3
from typing import Union
from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()

answer_list = ["YES", "NO", "MAYBE"]

class Question(BaseModel):
    question: str

def get_connection():
    return sqlite3.connect('questions.db')

@app.get("/8ball")
def get_answer():
    random_answer = random.choice(answer_list)
    return { "answer": random_answer}

@app.post("/8ball")
def add_answer(new_answer: str):
    answer_list.append(new_answer)
    return answer_list

@app.get("/questions")
def get_questions():
    connection = get_connection()
    cursor = connection.cursor()

    query = 'SELECT * from questions;'
    cursor.execute(query)
    results = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description] # Get column names from cursor description
    
    json_data = []
    for row in results:
        row_dict = dict(zip(column_names, row))
        json_data.append(row_dict)

    cursor.close()
    return json_data

@app.get("/questions/{id}")
def get_questions(id: int):
    connection = get_connection()
    cursor = connection.cursor()

    query = 'SELECT * from questions where id = ?;'
    cursor.execute(query,(id,))
    result = cursor.fetchone()

    column_names = [desc[0] for desc in cursor.description]
    
    json_data = dict(zip(column_names, result))

    cursor.close()
    return json_data

@app.post("/questions")
def add_question(body: Question):
    connection = get_connection()
    cursor = connection.cursor()

    sql = "insert into questions(question) values(?)"
    cursor.execute(sql,(body.question,))

    connection.commit()

    # Close the cursor after use
    cursor.close()

