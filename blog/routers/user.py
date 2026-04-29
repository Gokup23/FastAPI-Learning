from fastapi import APIRouter
from ..import database , schemas ,models

router = APIRouter
get_db = database.get_db
 