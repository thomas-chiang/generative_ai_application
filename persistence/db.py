from sqlmodel import create_engine

sqlite_file_name = "social_network.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=False)
