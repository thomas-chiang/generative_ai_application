import json
from data_extraction.util import clean_string, remove_invalid_escape
from sqlmodel import Session, select, SQLModel
from persistence.db import engine
from persistence.model import (
    MentionedAuthor,
    Post,
    Author,
    Brand,
    Product,
    MentionedBrand,
    MentionedProduct,
)


def parse_dataset():
    with open("test_data_social_network.json", "r") as file:
        data = file.read()
    json_objects = data[1:-1].strip().split("\n}\n{")
    json_objects = ["{" + obj + "}" for obj in json_objects]
    return [json.loads(obj) for obj in json_objects]


def find_products_and_brands_in_LLM_results():
    with open("LLM_result.txt", "r") as file:
        data = file.read()
    json_strings = data[7:-3].strip().split("``````json")
    brand_set = set()
    product_set = set()
    for json_string in json_strings:
        try:
            deserialized_data = json.loads(remove_invalid_escape(json_string))
            brand_set.update(deserialized_data.get("brand_names", []))
            product_set.update(deserialized_data.get("product_names", []))
        except Exception as e:
            print(e)
    return (brand_set, product_set)


def transform_data_set(data_set, brand_set, product_set):
    for data in data_set:
        brands = []
        products = []
        cleaned_data = clean_string(data["text"])
        for product in product_set:
            if product in cleaned_data:
                products.append(product)
        for brand in brand_set:
            if brand in cleaned_data:
                brands.append(brand)
        data["brands"] = brands
        data["products"] = products
    return data_set


def insert_into_sql_db(data):
    def find_or_create(session: Session, model: SQLModel, **kwargs):
        instance = session.exec(select(model).filter_by(**kwargs)).first()
        if not instance:
            instance = model(**kwargs)
            session.add(instance)

    with Session(engine) as session:
        for entry in data:
            find_or_create(session, Author, name=entry["author"])

            for mentioned_author in entry["mentionedAuthors"]:
                find_or_create(session, Author, name=mentioned_author)

            for brand in entry["brands"]:
                find_or_create(session, Brand, name=brand)

            for product in entry["products"]:
                find_or_create(session, Product, name=product)

            post = Post(
                id=entry["docId"],
                authorFollower=entry["authorFollower"],
                author=entry["author"],
                post_type=entry["postType"],
                publication_timestamp=entry["publicationTime"]["timestamp"],
                publication_gmt_date=entry["publicationTime"]["gmt_date"],
                comments=entry["comments"],
                text=entry["text"],
            )
            session.merge(post)

            for mentioned_author in entry["mentionedAuthors"]:
                mentioned_author_entry = MentionedAuthor(
                    post_id=entry["docId"], author=mentioned_author
                )
                session.merge(mentioned_author_entry)

            for brand in entry["brands"]:
                mentioned_brand_entry = MentionedBrand(
                    post_id=entry["docId"], brand=brand
                )
                session.merge(mentioned_brand_entry)

            for product in entry["products"]:
                mentioned_product_entry = MentionedProduct(
                    post_id=entry["docId"], product=product
                )
                session.merge(mentioned_product_entry)

        session.commit()
