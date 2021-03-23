from sqlalchemy_utils import create_database, database_exists
from database import engine

def add_db():
    if not database_exists(engine.url):
        create_database(engine.url)