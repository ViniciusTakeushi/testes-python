import json

def stringToObject():
    jsonString = '{"a": "AA", "b": "BB"}'

    objJson = json.loads(jsonString)

    return objJson

def findParameterJson(parameterToFind):
    jsonString = '{"a": "AA", "b": "BB"}'

    objJson = json.loads(jsonString)

    return objJson[parameterToFind]