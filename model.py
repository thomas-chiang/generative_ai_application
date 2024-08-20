from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from db import engine

class PublicationTime(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: int
    gmt_date: datetime
    post_id: Optional[int] = Field(default=None, foreign_key="post.docId")

    post: Optional["Post"] = Relationship(back_populates="publication_time")


class MentionedAuthor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    doc_id: int = Field(foreign_key="post.docId")
    author_name: str

    post: Optional["Post"] = Relationship(back_populates="mentioned_authors")


class Post(SQLModel, table=True):
    docId: int = Field(primary_key=True)
    authorFollower: int
    author: str
    postType: str
    publication_time: Optional[PublicationTime] = Relationship(back_populates="post")
    comments: int
    shares: int
    text: str
    mentioned_authors: List[MentionedAuthor] = Relationship(back_populates="post")
    brand_name: Optional[str] = None  # Make brand_name nullable
    product_name: Optional[str] = None  # Make product_name nullable


# Create the SQLite database and tables
SQLModel.metadata.create_all(engine)

