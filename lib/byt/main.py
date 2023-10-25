
from sqlalchemy.orm import relationship, backref
from sqlalchemy import PrimaryKeyConstraint, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import declarative_base


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)


class Area(Base):
    __tablename__ = "areas"
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    duty = Column(String())
    location = Column(String())

    user_id = Column(Integer(), ForeignKey("users.id"))

    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'Duty: {self.duty} ' \
        + f'Location: {self.location}'


class Equipment(Base):
    __tablename__ = "equipments"
    __table_args__ = (PrimaryKeyConstraint("id"), )

    id = Column(Integer())
    type = Column(String())

    user_id = Column(Integer(), ForeignKey("users.id"))

    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'Type: {self.type}'


class User(Base):
    __tablename__ = 'users'
    __table_args__ = (PrimaryKeyConstraint("id"), )
    
    id= Column(Integer())
    first_name = Column(String())
    last_name = Column(String())
    gender = Column(String())
    position = Column(String())

    
    equipments = relationship("Equipment", backref=backref('user'))
    areas = relationship("Area", backref=backref('user'))

    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'First Name: {self.first_name} ' \
        + f'Last Name: {self.last_name} ' \
        + f'Gender: {self.gender}' \
        + f'Position: {self.position} '

    def test(session, last_name):
        user = session.query(User).filter(User.last_name == last_name).first()
        print([record for record in user])