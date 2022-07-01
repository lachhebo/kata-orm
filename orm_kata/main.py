import datetime
from email.policy import default
from enum import unique
import os
from dotenv import load_dotenv
from sqlalchemy import Column, DateTime, Integer, String, create_engine

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

load_dotenv()
Base = declarative_base()
connection_string = os.getenv("CONNECTION_STRING")
engine = create_engine(connection_string)


def main():
    Base.metadata.create_all(engine)

    # create session and add objects
    with Session(engine) as session:
        elon = Person("Elon", "Musk",
            datetime.datetime(month=6, day=26, year=1971)
        )
        session.add(elon)
        session.commit()


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birthdate = Column(DateTime)
    isma = Column(DateTime)
    isma2 = Column(DateTime)

    def __repr__(self):
        return f"{self.id}"

    def __init__(self, name, surname, birthdate) -> None:
        self.name = name
        self.surname = surname
        self.birthdate = birthdate


if __name__ == "__main__":
    main()
