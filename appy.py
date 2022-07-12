import requests
from flask import Flask, request, jsonify
user_info=[{"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
    ]
app=Flask(__name__)


def iterate_id():
    return max(user_id['id'] for user_id in user_info)+1

@app.get("/user_info")
def get_it():
    return jsonify(user_info)

@app.post("/user_info")
def add_user():
    if request.is_json():
        user_id=request.get_json()
        user_id["id"] = iterate_id()
        user_info.append(user_id)
        return user_id
    return {"error": "Request must be JSON"}
