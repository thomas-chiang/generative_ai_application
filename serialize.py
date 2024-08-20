from llm_prompt import extract_info_from_100_posts
from extract_from_orginal import parsed_data

parsed_data = parsed_data

chunk_size = 100

for i in range(0, len(parsed_data), chunk_size):
    data = parsed_data[i:i+chunk_size]
    posts = [obj.get("text") for obj in data]
    info = extract_info_from_100_posts(posts)
    # Append info to identified_data.txt
    with open('identified_data.txt', 'a') as file:
        file.write(info)




