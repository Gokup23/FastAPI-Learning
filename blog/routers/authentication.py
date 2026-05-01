from fastapi import APIRouter , Depends
from .. import schemas , database , models
from sqlalchemy.orm import Session
router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:schemas.login , db: Session = Depends(database.get_db())):
    user = db.query(models.user).filter(models.user.email == request.username)
    if not user:
        raise 
    return 'login'