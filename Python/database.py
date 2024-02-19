# create_engine brukes til å opprette en forbindelse til databasen
from sqlalchemy import create_engine
# sessionmaker brukes til å opprette et session factory, som igjen brukes til å samhandle med databasen
from sqlalchemy.orm import sessionmaker
# declarative_base vil være klassen det arves fra når vi lager databaseentries fra python-objecter.
from sqlalchemy.ext.declarative import declarative_base


# String som definerer databasedialekt (sqlite) og plassering (./test.db).
url_database = "sqlite:///./test.db"



# Oppretting av SQLAlchemy engine. Parameteren connect_args={"check_same_thread":False} er her
# for at SQLite skal tillate at flere threads har samme forbindelse til databasen.
engine = create_engine(url_database, connect_args={"check_same_thread":False})



# Her opprettes en session factory 'SessionLocal'. En session er en gateway til databasen
# som brukes til å utstede queries/spørsmål til databasen eller manipulere
# data i databasen. autocommit=False og autoflush=False sørger for at SQLAlchemy 
# ikke begår endringer i databasen automatisk. bind=engine sørger for at denne sessionen
# er bundet opp til 'engine' som opprettholder forbindelse til databasen.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



# Oppretter en baseklasse som videre ORM-modeller skal arve fra. Greia til SQLAlchemy er at den lar oss
# opprette databasetabeller og beskrive forholdene mellom disse ved hjelp av python-objecter,
# uten at vi trenger å skrive en eneste linje SQL. ORM-modeller (object-relational mapping) vil i denne konteksten si 
# python-klasser som representerer databasetabeller, og hver instans av klassen representerer en rad i en slik tabell.
# Modellene brukt i denne databassen ligger i filen models.py.
Base = declarative_base()