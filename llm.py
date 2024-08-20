import vertexai
from vertexai.generative_models import GenerativeModel
import re
import os

project_id = os.getenv("YOUR_GCP_PROJECT_ID")

vertexai.init(project=project_id, location="asia-east1")

model = GenerativeModel("gemini-1.5-pro-001")

def extract_info_from_100_posts(posts):
    posts = posts[:100]
    posts = [re.sub(r'[\ud800-\udfff]', '', post) for post in posts]
    response = model.generate_content(
    f"""
        Identify the brand_name and the product_name in each of following posts: 
        {posts}
        and 
        please reply me with a json string of list of brand_names and product_names (both of them are treated like hashset with no duplicate values)
        example: ```json'{{' "brand_names":["Nike", "Puma"], "product_names": ["Shoes", "Vest", "t-shirt", "shorts"] '}}'```
    """
    )
    return response.text

