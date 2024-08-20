from sqlmodel import Session
from datetime import datetime
from extract_from_orginal import parsed_data as data
from db import engine
from model import PublicationTime, MentionedAuthor, Post


# Function to handle the insertion of multiple entries
def insert_entries(entries):
    with Session(engine) as session:
        for entry in entries:
            post = Post(
                docId=entry["docId"],
                authorFollower=entry["authorFollower"],
                author=entry["author"],
                postType=entry["postType"],
                comments=entry["comments"],
                shares=entry["shares"],
                text=entry["text"],
            )
            session.add(post)

            publication_time = PublicationTime(
                timestamp=entry["publicationTime"]["timestamp"],
                gmt_date=datetime.strptime(
                    entry["publicationTime"]["gmt_date"], "%Y-%m-%d %H:%M:%S.%f"
                ),
                post_id=post.docId,
            )
            session.add(publication_time)

            for mentioned_author in entry["mentionedAuthors"]:
                mentioned_author_entry = MentionedAuthor(
                    doc_id=post.docId, author_name=mentioned_author
                )
                session.add(mentioned_author_entry)

        # Commit all changes at once
        session.commit()

# Example usage with parsed data
insert_entries(data)
