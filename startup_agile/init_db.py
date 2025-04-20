from dotenv import load_dotenv
import os
from app.models.database import Base, engine
from app.models.entities import ResumeMatch
DB = os.getenv("DATABASE_URL")
print(DB)
Base.metadata.create_all(bind=engine)
