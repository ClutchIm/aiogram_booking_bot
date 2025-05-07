from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from db.connection import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String(100), nullable=False)
    table_id = Column(Integer, ForeignKey("tables.id", ondelete="CASCADE"), nullable=False)
    reservation_time = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, nullable=True)  # None = infinity reservation
    created_at = Column(DateTime, default=datetime.utcnow)

    table = relationship("Table", back_populates="reservations")

    def __repr__(self):
        return f"<Reservation by {self.customer_name} at {self.reservation_time}>"
