# API is about connecting data across the world
# Application Programming Interface
# How software can communicate with one another , e.g. one piece of software may need data from another area to work

# Client -> HTTP methods -> API -> HTTP request -> Server -> Your data -> API -> JSON
# Client sends method they want to use, API formats that into a proper request
# GET = request data
# API says: what content-type, what date the request it made, accepted character set
# HTTP request usually has no body, since you want something from the server
#JSON- language that practically every software can access and use
# API turns data sent back from server into JSON
#HTTP response:
# status code: success or not
# gives context around the server
# server sends back requested key:value pairs - formatted in JSON by API
# API turns the request

import requests
import json

# post_codes_req = requests.get"(https://api.postcodes.io/postcodes/se120nb")
#
# print(post_codes_req) # Output= <Response [200]>
#
# print(post_codes_req.status_code) # Output= 200
# print(post_codes_req.headers)  # Outputs = The raw http headers
# print(post_codes_req.content)  # Outputs = raw content
# print(post_codes_req.json())   # Outputs = get the content in JSON format
# print(type(post_codes_req.json())) # Output = <class 'dict'>

# Can specify the data we want
# Dump lets us set the data that we want to send to the API
#
json_body = json.dumps({"postcodes": ["PR8 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

# Don't need characters at the end because now we are asking for specific data from the API
post_multi_req = requests.post("https://api.postcodes.io/postcodes/", headers=headers, data=json_body)

print(post_multi_req.json())

# Important to check the documentation of the API you are requesting
#GET requests everything


