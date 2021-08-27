from sqlalchemy import Column, Integer, String, Text, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base


class Tour(Base):
    __tablename__ = 'tour'

    id = Column(Integer, autoincrement=True, primary_key=True)
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


class Departure(Base):
    __tablename__ = 'departure'

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String, nullable=True)
    abbr = Column(String, nullable=True)
    tour_id = Column(Integer, ForeignKey('tour.id'))

    def __repr__(self) -> str:
        return self._repr(abbr=self.title)
