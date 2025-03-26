from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DATABASE = 'postgresql://postgres:password@localhost:5432/quizapplicationyt'


engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()


# # import sqlalchemy as _sql
# # import sqlalchemy.ext.declarative as _declarative
# # import sqlalchemy.orm as _orm

# # DATABASE_URL = "postgresql://myuser:password@localhost/fastapi_database"

# # engine = _sql.create_engine(DATABASE_URL)

# # SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base = _declarative.declarative_base()


# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'postgresql://myuser:password@localhost:5432/fastapi_database'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()



# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()