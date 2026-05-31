from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date
from datetime import date

from app.database.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(100), nullable=False)

    amount = Column(Float, nullable=False)

    category = Column(String(50), nullable=False)

    transaction_type = Column(String(20), nullable=False)

    date = Column(Date, default=date.today)
