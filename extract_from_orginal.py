import json

# Read the content from the .txt file
with open('test_data_social_network.txt', 'r') as file:
    data = file.read()

# Split the string into individual JSON objects
json_objects = data[1:-1].strip().split('\n}\n{')

# Add necessary brackets to each object
json_objects = ['{' + obj + '}'  for obj in json_objects]

# Parse each JSON object into a Python dictionary
parsed_data = [json.loads(obj) for obj in json_objects]


print(parsed_data[0])

