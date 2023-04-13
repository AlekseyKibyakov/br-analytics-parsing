import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from config import DB_LOGIN
from models import create_tables, Project, Source

DSN = f'postgresql://{DB_LOGIN["login"]}:\
{DB_LOGIN["password"]}@{DB_LOGIN["host"]}:\
{DB_LOGIN["port"]}/{DB_LOGIN["database"]}'

engine = sq.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()


def _check_is_in_db(item):
    '''Check if item is in database'''
    if isinstance(item, Project):
        for project in session.query(Project).all():
            if project.theme_id == item.theme_id:
                return True
    return False


def add_to_db(item):
    if _check_is_in_db(item):
        session.close()
        return
    session.add(item)
    commit_session()


def commit_session():
    session.commit()


def close_session():
    session.close()