
from pathlib import Path
import sqlite3
import pandas as pd
from sqlalchemy import create_engine

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "data" / "database" / "superstore.db"


def get_connection():
    """Create a SQLite database connection."""
    return sqlite3.connect(str(DATABASE_PATH))


def get_engine():
    """Create a SQLAlchemy engine."""
    return create_engine(f"sqlite:///{DATABASE_PATH}")


def run_query(query, params=None):
    """Execute a SQL query and return results as a DataFrame."""
    with get_connection() as connection:
        return pd.read_sql_query(query, connection, params=params)