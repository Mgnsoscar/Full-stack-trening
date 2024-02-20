from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List, Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True, 
    allow_methods = ["*"],
    allow_headers=["*"]
)

class EmnerModel(BaseModel):
    emnekode: str
    navn: str
    studiepoeng: float
    emnekoordinator: str

    #class Config:
     #   orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)

# Lager et dummy endpoint
@app.get("/")
def get_root():
    return "Hallo Verden"

# Funksjon for å legge til nye emner i databasen.
@app.post("/emner", response_model = EmnerModel)
async def create_emne(emne: EmnerModel, db: db_dependency):
    emne = models.Emner(**emne.dict())
    db.add(emne)
    db.commit()
    db.refresh(emne)
    return emne

# Funksjon for å hente alle emner fra databasen
@app.get("/emner", response_model=List[EmnerModel])
async def read_emner(
        db: db_dependency
        ):

    query = db.query(models.Emner)
    emner = query.all()
    return emner

# Funksjon for å slette emner fra databasen basert på emnekode
@app.delete("/emner")
def slett_emne(emnekode: str, db: db_dependency):

    emne = db.query(models.Emner).filter(models.Emner.emnekode == emnekode).all()
    
    if len(emne) == 0:
        raise HTTPException(status_code=404, detail=f"Emnekode {emnekode} not found.")
    
    db.query(models.Emner).filter(models.Emner.emnekode == emnekode).delete()
    db.commit()

    return f"Emne {emne}"
    
@app.get("/emner/søk", response_model=EmnerModel)
async def søk_emnekode(emnekode: str, db: db_dependency):

    forespørsel = db.query(models.Emner).filter(models.Emner.emnekode == emnekode).all()

    if len(forespørsel) == 0:
        raise HTTPException(status_code=404, detail=f"Emne {emnekode} ikke funnet.")
    
    return forespørsel[0]