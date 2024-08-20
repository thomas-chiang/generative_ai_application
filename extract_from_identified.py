import json
import re
# Read the content from the .txt file
with open('identified_data.txt', 'r') as file:
    data = file.read()


# Split the string into individual JSON objects
json_objects = data[7:-3].strip().split('``````json')

# Add necessary brackets to each object
json_objects = [obj for obj in json_objects]

# Parse each JSON object into a Python dictionary
parsed_data = []
error_count = 1
for obj in json_objects:
    try:
        invalid_escape_pattern = r'\\(?!["\\/bfnrt])'
        cleaned_str = re.sub(invalid_escape_pattern, '', obj)
        parsed_data.append(json.loads(cleaned_str))
    except Exception as e:  
        print(error_count)
        error_count += 1
        print(e)
        print(obj)