from fastapi import HTTPException, status
from cachetools import TTLCache
import time
from src.core.logger import setup_logger

logger=setup_logger(__name__)

login_attempts_cache=TTLCache(maxsize=10000, ttl=600)
MAX_ATTEMPTS=5

def check_login_attempts(client_ip:str):
    attempt_record=login_attempts_cache.get(client_ip, [0,time.time()])
    attempt_count=attempt_record[0]

    if attempt_count>=MAX_ATTEMPTS:
        logger.warning("Warning: %s", f"IP address blocked due too many login attempts{client_ip}")
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many login try again after 10 minutes",)
    attempt_record[0] +=1
    login_attempts_cache[client_ip]=attempt_record

def reset_login_attempts(client_ip:str):
    if client_ip in login_attempts_cache:
        del login_attempts_cache[client_ip]