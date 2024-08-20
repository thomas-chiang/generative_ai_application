import json
import re
from json.decoder import JSONDecodeError

# Read the content from the .txt file
with open('identified_data.txt', 'r') as file:
    data = file.read()

# Split the string into individual JSON objects
json_objects = data[7:-3].strip().split('``````json')

# Add necessary brackets to each object
json_objects = [obj for obj in json_objects]

brand_set = set()
product_set = set()

errors = []
for obj in json_objects:
    try:
        invalid_escape_pattern = r'\\(?!["\\/bfnrt])'
        cleaned_str = re.sub(invalid_escape_pattern, '', obj)
        desirialized_data = json.loads(cleaned_str)
        brand_set.update(desirialized_data.get("brand_names", []))
        product_set.update(desirialized_data.get("product_names",[]))
    except Exception as e:
        errors.append(e)

print("Number of Errors: ", len(errors))

