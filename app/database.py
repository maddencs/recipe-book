from __future__ import annotations

import os

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)


# (Optional but recommended) Enforce FK constraints in SQLite
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # SQLite needs this pragma to actually enforce FOREIGN KEY constraints
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Session = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


class Base(DeclarativeBase):
    pass
