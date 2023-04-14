import sqlalchemy as sq
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

def create_tables(engine):
    Base.metadata.create_all(engine)

class Project(Base):
    __tablename__ = 'project'
    
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    theme_id = sq.Column(sq.VARCHAR(30), unique=True)
    name = sq.Column(sq.VARCHAR(100), unique=True)
    sources = relationship('Source', backref='project_sources')
    
    def __str__(self):
        return [
            self.id,
            self.theme_id,
            self.name,
            self.sources,
            ]

    
class Source(Base):
    __tablename__ = 'source'
    
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name = sq.Column(sq.VARCHAR(150))
    num_of_msgs = sq.Column(sq.Integer)
    percent = sq.Column(sq.Float)
    project_id = sq.Column(sq.Integer, sq.ForeignKey('project.id'))
    dates = relationship('Date', backref='source_dates')
    
    def __str__(self):
        return [
            self.id,
            self.name,
            self.num_of_msgs,
            self.percent,
            self.project_id,
            self.dates,
            self.project_sources,
            ]


# class Histogram(Base):
#     __tablename__ = 'histogram'
    
#     id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
#     source_id = sq.Column(sq.Integer, sq.ForeignKey('source.id'))
#     dates = relationship('Date', backref='histogram_dates')
    
#     def __str__(self):
#         return [
#             self.id, 
#             self.source_id,
#             self.dates,
#             self.source_histogram,
#             ]


class Date(Base):
    __tablename__ = 'date'
    
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    source_id = sq.Column(sq.Integer, sq.ForeignKey('source.id'))
    date = sq.Column(sq.DateTime)
    num_of_msgs = sq.Column(sq.Integer)
    tone_neutral = sq.Column(sq.Integer)
    tone_positive = sq.Column(sq.Integer)
    tone_negative = sq.Column(sq.Integer)
    
    def __str__(self):
        return [
            self.id,
            self.source_id,
            self.tone_negative,
            self.tone_neutral,
            self.tone_positive,
            self.source_dates,
            ]
