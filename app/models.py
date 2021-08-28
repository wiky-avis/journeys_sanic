from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String, Text, INTEGER
from sqlalchemy.orm import relationship
from app import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(INTEGER(), primary_key=True)


class Tour(BaseModel):
    __tablename__ = 'tour'

    title = Column(String)
    description = Column(Text, nullable=True)
    departure = Column(String, nullable=True)
    abbr = relationship(
        'Departure',
        primaryjoin='and_(Tour.id==Departure.tour_id, '
        'Departure.abbr==Tour.departure)')
    picture = Column(String, nullable=True)
    price = Column(Numeric(10, 2), nullable=True)
    stars = Column(Integer, nullable=True)
    country = Column(String, nullable=True)
    nights = Column(Integer, nullable=True)
    date = Column(Date, nullable=True)


class Departure(BaseModel):
    __tablename__ = 'departure'

    title = Column(String, nullable=True)
    abbr = Column(String, nullable=True)
    tour_id = Column(Integer, ForeignKey('tour.id'))

    def __repr__(self) -> str:
        return self._repr(abbr=self.title)
