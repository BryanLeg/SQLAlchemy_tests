from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Base class used by my classes (entities)
Base = declarative_base()

# Definition of Contact class
class Contact(Base):
    __tablename__= 'Contacts'

    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)

    def __init__(self, pk = 0, fn = "John", ln = "Doe"):
        self.id = pk
        self.first_name = fn
        self.last_name = ln

    def __str__(self):
        return self.first_name + " " + self.last_name
    
# Main part
if __name__ == "__main__":

    engine = create_engine('sqlite:///demo.db', echo = False)

    print("--- Construct all tables for the database (here just one table) ---" )
    Base.metadata.create_all(engine)

    print( "--- Create three new contacts and push its into the database ---" )
    Session = sessionmaker(bind=engine)
    session = Session()
