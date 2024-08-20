from sqlmodel import SQLModel, Field
from typing import  Optional
from data_extraction.db import engine


class Brand(SQLModel, table=True):
    name: str = Field(primary_key=True)


class MentionedBrand(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    post_id: int = Field(foreign_key="post.id")
    brand: str = Field(foreign_key="brand.name")


class Product(SQLModel, table=True):
    name: str = Field(primary_key=True)


class MentionedProduct(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    post_id: int = Field(foreign_key="post.id")
    product: str = Field(foreign_key="product.name")


class Author(SQLModel, table=True):
    name: str = Field(primary_key=True)


class MentionedAuthor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    post_id: int = Field(foreign_key="post.id")
    author: str = Field(foreign_key="author.name")


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    authorFollower: Optional[int]
    author: str = Field(foreign_key="author.name")
    post_type: str
    publication_timestamp: int
    publication_gmt_date: str
    comments: Optional[int]
    text: Optional[str]



# Create the SQLite database and tables
SQLModel.metadata.create_all(engine)

