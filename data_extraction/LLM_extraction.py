import vertexai
from vertexai.generative_models import GenerativeModel
import re
import os
from data_extraction.function import parse_dataset

project_id = os.getenv("your_gcp_project_id")

vertexai.init(project=project_id, location="asia-east1")

model = GenerativeModel("gemini-1.5-pro-001")


def extract_info_from_100_posts(posts):
    posts = posts[:100]
    posts = [re.sub(r"[\ud800-\udfff]", "", post) for post in posts]
    response = model.generate_content(
        f"""
        Identify the brand_name and the product_name in each of following posts: 
        {posts}
        and 
        please reply me with a json string of list of brand_names and product_names (both of them are treated like hashset with no duplicate values)
        example: ```json'{{' "brand_names":["Nike", "Puma"], "product_names": ["Shoes", "Vest", "t-shirt", "shorts"] '}}'``` (Expecting property name enclosed in double quotes)
    """
    )
    return response.text


def create_LLM_result():
    parsed_data = parse_dataset()
    chunk_size = 100
    filename = "LLM_result.txt"
    with open(filename, "w") as file:
        file.write("")

    for i in range(0, len(parsed_data), chunk_size):
        data = parsed_data[i : i + chunk_size]
        posts = [obj.get("text") for obj in data]
        info = extract_info_from_100_posts(posts)
        with open(filename, "a") as file:
            file.write(info)
