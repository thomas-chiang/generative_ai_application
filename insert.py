from sqlmodel import Session, select, SQLModel
from merge_identified_data import merged_data as data
from data_extraction.db import engine
from model import  MentionedAuthor, Post, Author, Brand, Product, MentionedBrand, MentionedProduct

def get_or_create(session: Session, model: SQLModel, **kwargs):
    instance = session.exec(select(model).filter_by(**kwargs)).first()
    if not instance:
        instance = model(**kwargs)
        session.add(instance)
    return instance


# Function to handle the insertion of multiple entries
def insert_entries(entries):
    with Session(engine) as session:
        for entry in data:
            # Ensure the author exists in the Author table
            get_or_create(session, Author, name=entry['author'])

            # Ensure all mentioned authors exist in the Author table
            for mentioned_author in entry['mentionedAuthors']:
                get_or_create(session, Author, name=mentioned_author)

            # Ensure all mentioned brands exist in the Brand table
            for brand in entry['brands']:
                get_or_create(session, Brand, name=brand)

            # Ensure all mentioned products exist in the Product table
            for product in entry['products']:
                get_or_create(session, Product, name=product)

            # Create and add the Post entry
            post = Post(
                id=entry['docId'],
                authorFollower=entry['authorFollower'],
                author=entry['author'],
                post_type=entry['postType'],
                publication_timestamp=entry['publicationTime']['timestamp'],
                publication_gmt_date=entry['publicationTime']['gmt_date'],
                comments=entry['comments'],
                text=entry['text']
            )
            session.add(post)

            # Add mentioned authors for the post
            for mentioned_author in entry['mentionedAuthors']:
                mentioned_author_entry = MentionedAuthor(
                    post_id=entry['docId'],
                    author=mentioned_author
                )
                session.add(mentioned_author_entry)

            # Add mentioned brands for the post
            for brand in entry['brands']:
                mentioned_brand_entry = MentionedBrand(
                    post_id=entry['docId'],
                    brand=brand
                )
                session.add(mentioned_brand_entry)

            # Add mentioned products for the post
            for product in entry['products']:
                mentioned_product_entry = MentionedProduct(
                    post_id=entry['docId'],
                    product=product
                )
                session.add(mentioned_product_entry)

        session.commit()

# Example usage with parsed data
insert_entries(data)
