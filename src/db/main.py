# Inside src/db/main.py
from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

from src.config import Config
from sqlmodel import SQLModel
from src.books.models import Book


# engine = AsyncEngine(create_engine(
#     url=Config.DATABASE_URL,
#     echo=True
# ))

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo= True
)


async def initdb():
    """create our database models in the database"""

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)        