from flask import Blueprint, request
from shared.functions import response, readJson, writeJson
import uuid

todos = Blueprint("todos", __name__)

@todos.route("/")
def getAll():
    data = {
        "message": "Done!",
        "data": readJson("todos.json")
    }
    return response(data, 200)

@todos.route("/getById", methods=["GET"])
def getById():
    # parametros por url
    # EJ localhost:4000/api/todo/getById?id=2
    id = request.args.get("id")
    data = readJson("todos.json")
    todo = {}
    for d in data:
        if str(d["id"]) == str(id):
            todo = d
            break

    return response({ "message": "", "data": todo}, 200)

@todos.route("/insert", methods=["POST"])
def insert():
    data = readJson("todos.json")
    # obtener info del body
    body = request.json
    body["id"] = str(uuid.uuid4())
    data.append(body)
    writeJson("todos.json", data)
    return response({ "message": "Todo Created", "data": [] }, 200)

@todos.route("/update", methods=["PUT"])
def update():
    data = readJson("todos.json")
    # obtener info del body
    id = request.args.get("id")
    body = request.json
    for d in data:
        if str(d["id"]) == str(id):
            d["title"] = body["title"]
            d["description"] = body["description"]
            break
    writeJson("todos.json", data)
    return response({ "message": "Todo Created", "data": [] }, 200)

@todos.route("/delete", methods=["DELETE"])
def delete():
    data = readJson("todos.json")
    # obtener info del body
    id = request.args.get("id")
    for i in range(len(data)):
        if str(data[i]["id"]) == str(id):
            del data[i]
            break
    writeJson("todos.json", data)
    return response({ "message": "Todo Created", "data": [] }, 200)