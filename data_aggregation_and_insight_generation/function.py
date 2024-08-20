from sqlmodel import Session, select, func
from persistence.model import Post, MentionedAuthor, MentionedBrand, MentionedProduct
from persistence.db import engine
from sqlalchemy import desc
import csv


def export_to_csv(filename, data, headers):
    filename = "CSV_files/" + filename
    with open(filename, "w") as file:
        file.write("")

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


def analyze():
    with Session(engine) as session:
        # 1. Top 10 Mentioned Authors
        statement = (
            select(
                MentionedAuthor.author,
                func.count(MentionedAuthor.author).label("mention_count"),
            )
            .group_by(MentionedAuthor.author)
            .order_by(desc("mention_count"))
            # .limit(10)
        )
        top_authors = session.exec(statement).all()
        export_to_csv("top_mentioned_authors.csv", top_authors, ["Author", "Mentions"])

        # 2. Top 10 Mentioned Brands
        statement = (
            select(
                MentionedBrand.brand,
                func.count(MentionedBrand.brand).label("mention_count"),
            )
            .group_by(MentionedBrand.brand)
            .order_by(desc("mention_count"))
            # .limit(10)
        )
        top_brands = session.exec(statement).all()
        export_to_csv("top_mentioned_brands.csv", top_brands, ["Brand", "Mentions"])

        # 3. Top 10 Mentioned Products
        statement = (
            select(
                MentionedProduct.product,
                func.count(MentionedProduct.product).label("mention_count"),
            )
            .group_by(MentionedProduct.product)
            .order_by(desc("mention_count"))
            # .limit(10)
        )
        top_products = session.exec(statement).all()
        export_to_csv(
            "top_mentioned_products.csv", top_products, ["Product", "Mentions"]
        )

        # 4. Number of Posts per Author
        statement = (
            select(Post.author, func.count(Post.id).label("post_count"))
            .group_by(Post.author)
            .order_by(desc("post_count"))
        )
        posts_per_author = session.exec(statement).all()
        export_to_csv(
            "posts_per_author.csv", posts_per_author, ["Author", "Post Count"]
        )

        # 5. Number of Posts per Post Type
        statement = (
            select(Post.post_type, func.count(Post.id).label("post_count"))
            .group_by(Post.post_type)
            .order_by(desc("post_count"))
        )
        posts_per_type = session.exec(statement).all()
        export_to_csv("posts_per_type.csv", posts_per_type, ["Post Type", "Post Count"])

        # 6. Distribution of Posts Over Time (e.g., by month)
        statement = (
            select(
                func.strftime("%Y-%m", Post.publication_gmt_date).label("month"),
                func.count(Post.id).label("post_count"),
            )
            .group_by("month")
            .order_by("month")
        )
        posts_over_time = session.exec(statement).all()
        export_to_csv("posts_over_time.csv", posts_over_time, ["Month", "Post Count"])
