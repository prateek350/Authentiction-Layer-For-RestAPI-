import os 
from dotenv import load_dotenv,find_dotenv

dotenv_path=find_dotenv()
load_dotenv(dotenv_path, override=True)

class Settings:
    """It is used to import the essential keys and version of the app"""

    PROJECT_TITLE: str="Authentication Layer"
    PROJECT_VERSION:str="0.1.0"

    USER:str=os.getenv("PG_USERNAME")
    PASSWORD:str=os.getenv("PG_PASSWORD")
    SERVER: str=os.getenv("PG_HOST")
    PORT:str=os.getenv("PG_PORT")
    DB:str=os.getenv("PG_DB")
    DATABASE_URL:str=f"postgresql+asyncpg://{USER}: (PASSWORD)@(SERVER): (PORT)/{DB}"
    
    SECRET_KEY:str=os.getenv("SECRET_KEY")
    ALGORITHM: str="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int=30