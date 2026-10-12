
from pathlib import Path
import sqlite3
from sqlalchemy import create_engine

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "data" / "database" / "superstore.db"


def get_sqlite_connection():
    """Connect to the Superstore SQLite database."""
    return sqlite3.connect(str(DATABASE_PATH))


def get_sqlalchemy_engine():
    """Create a SQLAlchemy engine for the database."""
    return create_engine(f"sqlite:///{DATABASE_PATH}")


if __name__ == "__main__":
    with get_sqlite_connection() as connection:
        result = connection.execute(
            "SELECT COUNT(*) FROM superstore;"
        ).fetchone()

    print("Database connection successful!")
    print(f"Total records: {result[0]}")
