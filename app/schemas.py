from pydantic import BaseModel

class EntryBase(BaseModel):
    link: str
    xpath: str
    value: str
    alias: str

class EntryCreate(EntryBase):
    pass

class Entry(EntryBase):
    id: int

    class Config:
        from_attributes = True