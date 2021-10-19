from flask import jsonify
import json

def response(body: dict, status_code: int):
    response = jsonify(body)
    response.status_code = status_code
    return response

def readJson(nameFile):
    with open("./shared/"+nameFile, "r") as file:
        return json.load(file)

def writeJson(nameFile, data):
    with open("./shared/"+nameFile, "w") as file:
        json.dump(data, file)
        file.close()
        return True