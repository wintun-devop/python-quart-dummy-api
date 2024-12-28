import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#to get to ensure from .env
load_dotenv(override=True)

# getting data from env
db_name=os.getenv("DB_NAME")
db_user=os.getenv("DB_USER")
db_password=os.getenv("DB_PASSWORD")
db_host=os.getenv("DB_HOST")

db_link = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}"

engine = create_engine(db_link)
Session = sessionmaker(bind=engine)
db_session = Session()