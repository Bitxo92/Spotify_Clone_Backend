from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker





DATABASE_URL="postgresql://root:root@localhost:5432/flutter_music_app"
engine = create_engine(DATABASE_URL)
SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db(): #dependency inyection
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()


