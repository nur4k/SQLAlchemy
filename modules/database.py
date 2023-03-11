from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем объект Engine для работы с базой данных
engine = create_engine('postgresql://postgres:@localhost/example_db', echo=True)

# Создаем класс модели данных, который будет представлять таблицу в базе данных
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

def create_db():
    Base.metadata.create_all(engine)
