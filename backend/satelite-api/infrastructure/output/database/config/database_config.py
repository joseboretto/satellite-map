from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from infrastructure.config.env import get_environment_variables

# Runtime Environment Configuration
env = get_environment_variables()

DATABASE_SCHEMA = 'satellite'
# Create Database Engine
Engine = create_engine(
    env.DATABASE_URL, echo=env.DEBUG_MODE, future=True,
    connect_args={'options': '-csearch_path={}'.format(DATABASE_SCHEMA)}
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=Engine
)


def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()
