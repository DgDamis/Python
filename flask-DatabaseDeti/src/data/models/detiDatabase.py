from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime,Float

from ..database import db
from ..mixins import CRUDModel
from sqlalchemy.types import Date

class Deti(CRUDModel):
    __tablename__ = 'deti'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    jmeno = Column(String(64), nullable=False, index=False)
    prijmeni = Column(String(64), nullable=False, index=True)
    datumNarozeni = Column(Date)
    # Use custom constructor
    # pylint: disable=W0231


