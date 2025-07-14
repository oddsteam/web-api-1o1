from fastapi import FastAPI

app = FastAPI(
    title="Let's find the answer",
    description="A fun fortune-telling API that gives you random answers like a Magic 8 Ball."
)

answer_list = ["YES", "NO", "MAYBE"]

@app.get("/8ball")
def get_answer():
    ## TODO: Random answer
    return { "answer": "Okay inw za"}

@app.post("/8ball")
def add_answer(new_answer: str):
    ## TODO: Update list of answer with new_answer
    return answer_list
