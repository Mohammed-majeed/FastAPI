from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    DATABASE_HOSTNAME:str
    DATABASE_PORT:str
    DATABASE_PASSWORD:str
    DATABASE_NAME:str
    DATABASE_USERNAME:str
    
    SECRET_KEY:str
    ALGORITHIM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int

    class Config:
        env_file=".env"

setting = Setting()
print(setting.SECRET_KEY)