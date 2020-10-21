import json

import logging

import requests

import jsonschema
from jsonschema import validate




# Describe what kind of json you expect.

expctedSchema = {
    "type": "object",
    "properties": {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"},
    },
}

#
# GET service
# https://jsonplaceholder.typicode.com/posts
# - verify that status code is 200
# - verify the schema
# - verify that API returns at least 100 records
# - verify the schema

# GET service
def test_Get_Status():
    # GET service
    response = requests.get("https://jsonplaceholder.typicode.com/posts", params={'AuthorName': 'Arun gupta'})

    dict_response = json.loads(response.text)

    json_response = response.json()

    # - verify that status code is 200
    assert response.status_code == 200
    print(response.status_code)
    log = get_logging()
    logMsg = "GET status code :", response.status_code
    log.info( logMsg)
    # - verify that API returns at least 100 records
    numberRecords = len(dict_response)
    print(numberRecords)
    assert numberRecords == 100
    logMsg = "API returns records:", numberRecords

    log.info(logMsg)


    # validate  schema
    isValid = validateSchema(dict_response)

    print("Given JSON string is Valid:", isValid)



    # https://jsonplaceholder.typicode.com/posts/1
    # - verify that status code is 200
    # - verify the schema
    # - verify that API returns only one record
    # - verify that id in response matches the input (1)

    # GET service
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", params={'AuthorName': 'Arun gupta'})

    dict_response = json.loads(response.text)

    json_response = response.json()

    # - verify that status code is 200
    assert response.status_code == 200
    logMsg = "Status code : ", response.status_code
    log.info(logMsg)

    # verify that API returns only one record
    numberR = len(dict_response)

    assert numberR == 4

    # - verify the schema

    dict_response = json.loads(response.text)

    # validate it
    isValid = validateSchema(dict_response)
    logMsg = "Given JSON string is Valid", isValid

    log.info(logMsg)



    # verify that id in response matches the input (1)

    assert json_response['id'] == 1

    #
    # https://jsonplaceholder.typicode.com/invalidposts
    # - verify that status code is 404
    # - log the complete request and response details for troubleshooting

    # GET service
    response = requests.get("https://jsonplaceholder.typicode.com/invalidposts", params={'AuthorName': 'Arun gupta'})

    dict_response = json.loads(response.text)

    json_response = response.json()

    # - verify that status code is 404
    assert response.status_code == 404
    logMsg= "status code : ", response.status_code
    log.info(logMsg)

    dict_response = json.loads(response.text)


    # validate it
    isValid = validateSchema(dict_response)

    print("Given JSON string is Valid", isValid)

    logMsg = "Given JSON string is Valid", isValid
    log.info(logMsg)



    # - log the complete request and response details for troubleshooting
    print(dict_response)

# POST service
def test_Post_Status():
    url = 'https://jsonplaceholder.typicode.com/posts'
    headers = {"Content-Type": "application/json"}
    post_response = requests.post(url, json={
        "title": "foo",
        "body": "bar",
        "userId": 1
    }, headers=headers, )

    print(post_response.json())

    print(post_response.status_code)

    assert post_response.status_code == 201

    log = get_logging()
    logMsg= "Verify POST status:", post_response.status_code
    log.info(logMsg)

    # - verify the schema

    dict_response = json.loads(post_response.text)


    # validate it
    isValid = validateSchema(dict_response)

    logMsg ="Given JSON string is Valid", isValid

    log.info(logMsg)

    # verify the record created
    json_response = post_response.json()
    assert json_response['userId'] == 1

# PUT service
def test_Put_status():
    # PUT service
    # https://jsonplaceholder.typicode.com/posts/1
    # body = {
    # "id": 1,
    # "title": "abc",
    # "body": "xyz",
    # "userId": 1
    # }
    # send body as JSON
    # - verify that status code is 200
    # - verify the schema
    # - verify the record updated

    url = ' https://jsonplaceholder.typicode.com/posts/1'
    headers = {"Content-Type": "application/json"}
    put_response = requests.put(url, json={
        "id": 1,
        "title": "abc",
        "body": "xyz",
        "userId": 1
    }, headers=headers, )

    print(put_response.json())

    print(put_response.status_code)

    assert put_response.status_code == 200


    log = get_logging()
    logMsg="Verify PUT status:", put_response.status_code
    log.info(logMsg)

    # - verify the schema
    # def validateJSON(jsonData):
    #     try:
    #         json.loads(jsonData)
    #     except ValueError as err:
    #         return False
    #     return True

    dict_response = json.loads(put_response.text)


    # validate it
    isValid = validateSchema(dict_response)

    print("Given JSON string is Valid", isValid)
    logMsg = "Given PUT  JSON string is Valid", isValid
    log.info(logMsg)


    # verify the record created
    json_response = put_response.json()
    assert json_response['userId'] == 1

    logMsg = "verify the record created : ", json_response['userId']
    log.info(logMsg)


# DELETE service
def test_Delete_Status():
    # DELETE service
    # https://jsonplaceholder.typicode.com/posts/1
    # - verify that status code is 200
    # - verify the

    delurl = 'https://jsonplaceholder.typicode.com/posts/1'
    response_delete = requests.delete(delurl, json={"userId": 1}, headers={"content/type": "application/json", "charset": "UTF-8"}, )

    print(response_delete.status_code)
    assert response_delete.status_code == 200
    log = get_logging()
    logMsg = "GET DELETE STATUS CODE:", response_delete.status_code
    log.info(logMsg)

    res_json = response_delete.json()
    print(res_json)
    print("Execution completed")





def validateSchema(dict_response):
    try:
        validate(instance=dict_response, schema=expctedSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True
    if isValid:
        print(isValid)
        # print("Given JSON data is Valid")
    else:
        print(isValid)
        # print("Given JSON data is InValid")


def get_logging():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  #filehandler object

    logger.setLevel(logging.INFO)

    return logger