# Import the create_engine function from SQLAlchemy.
# This function creates an Engine object, which is a factory for DB-API connections.
from sqlalchemy import create_engine

# Import the declarative_base helper from SQLAlchemy’s ORM layer.
# It returns a base class that all of your model classes will inherit from.
from sqlalchemy.ext.declarative import declarative_base

# Import sessionmaker, a configurable factory for creating Session objects.
# A Session manages ORM-level “conversations” with the database.
from sqlalchemy.orm import sessionmaker


# Define the database connection URL.
# Format: dialect+driver://username:password@host:port/database
# Here we are using SQLite with a relative file path (“./blog.db”).
SQLALCHEHY_DATABASE_URL = 'sqlite:///./blog.db'


# Create the Engine instance that knows how to connect to the database.
# For SQLite we pass connect_args with check_same_thread=False
# so the same connection can be shared safely across multiple threads
# (handy when using frameworks like FastAPI that may spawn background threads).
engine = create_engine(
    SQLALCHEHY_DATABASE_URL,
    connect_args={'check_same_thread': False}
)


# Configure the sessionmaker factory.
# autocommit=False  → you must explicitly call session.commit()
# autoflush=False   → prevents automatic flush before every query,
#                     giving you finer control and sometimes better performance.
# bind=engine       → ties every Session produced by this factory to the Engine above.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Generate a base class for declarative models.
# Every ORM model (e.g., User, Post, Comment) should inherit from this Base
# so SQLAlchemy can collect metadata and map classes to tables.
Base = declarative_base()
