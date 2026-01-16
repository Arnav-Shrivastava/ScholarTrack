from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models here so Alembic can detect them later
from app.models.user import User
