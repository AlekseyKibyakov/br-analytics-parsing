import sqlalchemy as sq
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

def create_tables(engine):
    Base.metadata.create_all(engine)

class Project(Base):
    __tablename__ = 'projects'
    
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    theme_id = sq.Column(sq.VARCHAR(30), unique=True)
    name = sq.Column(sq.VARCHAR(100), unique=True)
    sources = relationship('Source', back_populates='project')
    
    def __str__(self):
        return [
            self.id,
            self.name,
            self.sources,
            ]

    
class Source(Base):
    __tablename__ = 'sources'
    
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name = sq.Column(sq.VARCHAR(150))
    num_of_msgs = sq.Column(sq.Integer)
    percent = sq.Column(sq.Float)
    project_id = sq.Column(sq.Integer, sq.ForeignKey('projects.id'))
    project = relationship('Project', back_populates='sources')
    
    def __str__(self):
        return [
            self.id, 
            self.name, 
            self.num_of_msgs, 
            self.percent,
            self.project_id,
            ]


# class Histogram(Base):
#     __tablename__ = 'histogram'
    
#     id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
#     date = sq.Column(sq.VARCHAR(50))
#     name = sq.Column(sq.VARCHAR(150))
#     num_of_msgs = sq.Column(sq.Integer)
#     percent = sq.Column(sq.Float)
#     projects = relationship('Project', secondary='project_source', backref='sources', cascade='delete')
    
#     def __str__(self):
#         return [
#             self.id, 
#             self.name, 
#             self.num_of_msgs, 
#             self.percent,
#             self.projects,
#             ]
        
        
# project_source = sq.Table(
#     'project_source',
#     Base.metadata,
#     sq.Column('project_id', sq.ForeignKey('project.id', ondelete='CASCADE')),
#     sq.Column('source_id', sq.ForeignKey('source.id', ondelete='CASCADE')),
# )