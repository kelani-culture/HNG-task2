import requests

"""
This module serves as the client for the server
sends request and receives a response
"""
# send a post request method
def post_request():
    endpoint = "http://localhost:8000/api/"
    response = requests.post(endpoint, json={"name": "mark"})
    print(response.text)


# send a get request method
def get_request():
    endpoint = "http://localhost:8000/api/1"
    response = requests.get(endpoint)
    print(response.text)

def put_request():
    endpoint = "http://localhost:8000/api/9260"
    response = requests.put(endpoint, json={"name": "becca"})
    print(response.text)

def delete_request():
    endpoint = "http://localhost:8000/api/8220"
    res = requests.delete(endpoint)
    print(res.text)


if __name__ == "__main__":
    #delete_request()
    #put_request()
    #get_request()
    post_request()