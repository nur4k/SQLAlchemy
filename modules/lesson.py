from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from modules.database import Base


association_table = Table('association', Base.metadata, 
                        Column('lesson_id', Integer, ForeignKey('lessons.id')),
                        Column('group_id', Integer, ForeignKey('groups.id'))
                        )

class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True)
    lesson_title = Column(String)
    group = relationship('Group', secondary=association_table, backref='group_lesson')

    def __repr__(self) -> str:
        return f'Предмет [ID: {self.id} Название: {self.lesson_title}]'
