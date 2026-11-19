from fastapi import FastAPI

app = FastAPI(title = "SACCO API")

@app.get("/")
def home():
    return {"message" : "SACCO API is running"}

@app.get("/members")
def list_members():
    return[
        {"id": 1, "name" : "Blair Johns"},
        {"id": 2, "name": "Johns Carter"},
    ]