from sqlalchemy.orm import Session

from . import models, schemas

def get_entries(db: Session):
    return db.query(models.Entry).all()

def del_entry(db: Session, id: int):
    entry = db.query(models.Entry).filter_by(id=id).delete()
    if not entry: 
        return {'msg': f'Entry with ID:{id} not found.'}
    db.commit()
    return {'msg': f'Entry with ID:{id} deleted successfully.'}

def add_entry(db: Session, entry: schemas.EntryCreate):
    try:
        db_entry = models.Entry(link=entry.link,
                            xpath=entry.xpath,
                            value=entry.value,
                            alias=entry.alias)
        db.add(db_entry)
        db.commit()
        db.refresh(db_entry)
        return {'msg': f'Entry added successfully.'}
    except Exception as e:
        return {'msg': f'Failed to add entry: {e}'}