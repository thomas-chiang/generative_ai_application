import vertexai
from vertexai.generative_models import GenerativeModel
import re
import os

project_id = os.getenv("YOUR_GCP_PROJECT_ID")

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


brand_set = {"Nikes", "Adidias"}
product_set = {"jacket", "shoes"}


data = {
    "docId": 1,
    "authorFollower": 12200,
    "author": "JibreelDia",
    "postType": "retweet",
    "publicationTime": {
        "timestamp": 1719727087000,
        "gmt_date": "2024-06-30 05:58:07.000",
    },
    "mentionedAuthors": [],
    "comments": 2506,
    "shares": 5967,
    "text": "New shoes and jacket I bought yesterday! Y'all know I love my Nikes and Adidias 😁 https://t.co/FvQG4CKoBD",
}

I want to extract text field from data checkect if each word in text is in brand_set or product_set, 
if in, update the data with new key 'brands': [brand...] and  new key 'product': [product...]