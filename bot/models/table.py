from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from bot.db.connection import Base


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    seats = Column(Integer, nullable=False)
    location = Column(String(100), nullable=True)

    reservations = relationship(
        "Reservation",
        back_populates="table",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Table {self.name}>"
