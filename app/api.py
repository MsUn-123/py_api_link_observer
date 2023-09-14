from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/entries/all", response_model=list[schemas.Entry])
def get_all_entries(db: Session = Depends(get_db)):
    entries = crud.get_entries(db=db)
    return entries

@app.post("/entries/add")
def add_entry(entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    result = crud.add_entry(db=db, entry=entry)
    return result

@app.delete("/entries/delete/{entry_id}") #todo
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    result = crud.del_entry(db=db, id=entry_id)
    return result


if __name__ == "__main__":
    app.run() #it doesnt work????? LULE 