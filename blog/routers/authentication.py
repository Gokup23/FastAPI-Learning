from fastapi import APIRouter , Depends , HTTPException , status
from .. import schemas , database , models
from sqlalchemy.orm import Session
router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:schemas.login , db: Session = Depends(database.get_db)):
    user = db.query(models.user).filter(models.user.email == request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid credentials")
    return 'login'