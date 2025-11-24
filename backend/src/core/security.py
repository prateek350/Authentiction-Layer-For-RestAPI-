from datetime import datetime
from jose import jwt
from src.core.config import Settings

async def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now()+Settings.ACCESS_TOKEN_EXPIRE_MINUTES
    to_encode.update({"exp":expire})
    encode_jwt=jwt.encode(to_encode,Settings.SECRET_KEY,algorithm=Settings.ALGORITHM)
    return encode_jwt