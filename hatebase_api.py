''' This is the code for using the Hatebase API
It uses this Python wrapper: https://github.com/DanielJDufour/hatebase
which can be installed with: pip install hatebase

'''
from json import loads
from hatebase import HatebaseAPI

key = # get a key here: https://www.hatebase.org/request_api

# Define parameters
hatebase = HatebaseAPI({"key": key})
filters = {'language': 'eng'}
output = 'json'
query_type = 'sightings'

# Query the database
response = hatebase.performRequest(filters, output, query_type)

# Convert to Python object
resp = loads(response)