from database.database import engine
from database import models

def create_all_tables():
    print("Creating all tables...")
    models.Base.metadata.create_all(bind=engine)