from sqlmodel import Session, select
from model import Post
from db import engine

def get_posts_with_comments_above_threshold(threshold):
    with Session(engine) as session:
        # Construct the query
        statement = select(Post).where(Post.comments > threshold)
        results = session.exec(statement)
        return results.fetchall()

# Example usage
posts_above_threshold = get_posts_with_comments_above_threshold(2998)
for post in posts_above_threshold:
    print(post)