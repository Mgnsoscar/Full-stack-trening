# Importer Base-klassen som ble opprettet i database.py.
from database import Base
# Importer datatyper fra sqlalchemy. Collumn representerer kolonnene i databasetabellen.
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey


class Emner(Base):

    __tablename__ = "Emner"

    emnekode = Column("emnekode", String, primary_key=True, index=True)
    navn = Column("navn", String)
    studiepoeng = Column("studiepoeng", Float)
    emnekoordinator = Column("emnekoordinator", String)
