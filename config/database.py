from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

def get_engine(test_connection: bool = True):
    DB_HOST = os.getenv('DB_HOST_PROD')
    DB_PORT = os.getenv('DB_PORT_PROD')
    DB_NAME = os.getenv('DB_NAME_PROD')
    DB_USER = os.getenv('DB_USER_PROD')
    DB_PASS = os.getenv('DB_PASS_PROD')

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DATABASE_URL)

    # Trying connection
    if test_connection:
        try:
            with engine.connect() as conn:
                print("Conexão com SQLAlchemy bem-sucedida!")
        except Exception as e:
            print("Erro ao conectar:", e)
    return engine

if __name__ == "__main__":
    engine = get_engine(test_connection=True)