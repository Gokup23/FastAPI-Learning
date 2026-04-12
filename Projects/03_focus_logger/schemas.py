from pydantic import BaseModel

class SubjectBase(BaseModel):
    title:str
    is_active: bool = True

class SubjectCreate(SubjectBase):
    pass

class SubjectResponse(SubjectBase):
    id:int

    class Config:
        from_attributes = True