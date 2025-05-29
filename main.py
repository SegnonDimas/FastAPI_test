from fastapi import FastAPI
from typing import Union

app = FastAPI()

initial_root = "/"
all_users_endpoint = "/users"

@app.get(initial_root)
def read_root():
    return {"message": "Bienvenue dans mon API FastAPI!"}

@app.get(all_users_endpoint)
def all_users():
    return [
        {
            "id":1,
            "name": "Denis",
            "specialite" : "Dev"
        },
         {
            "id":2,
            "name": "Claudia",
            "specialite" : "Dev"
        },
         {
            "id":3,
            "name": "Ronhel",
            "specialite" : "Flutter"
        },
         {
            "id":4,
            "name": "Bertrand",
            "specialite" : "Dev"
        },
    ]

@app.get("/users/{id}")
def a_user(id) :
    return {
        "utilisateur" : id
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.delete("/users/{id}", description="Supprimer un utilisateur")
def delete_user(id : str):
    return {"message" : "L'utilisateur a été supprimé avec succès"}

@app.get("/users/me")
def myself():
    return {"message" : "This is me"}

@app.post("/users")
def new_user():
    return {"message" : "Utilisateur crée avec succès"}