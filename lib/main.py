from datetime import datetime

from sqlalchemy import  Column, Integer, String,DateTime, create_engine
from sqlalchemy.orm import  declarative_base, sessionmaker


Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'
    
    id= Column(Integer, primary_key =True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    position = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow)
    
    
    @property
    def full_name(self):
        return f'{self.first_name}  {self.last_name}'
    
    
    def __repr__(self):
        return(
            f'UserModel(id={self.id}, first_name={self.first_name},'
            f'last_name={self.last_name}, gender={self.gender},'
            f'created={self.created}')
            
    
user = [
    UserModel(first_name = 'Bob', last_name='James', gender='M'),
    UserModel(first_name = 'Biden', last_name='Jones', gender='M'),
    UserModel(first_name = 'Fred', last_name='Don', gender='M'),
    UserModel(first_name = 'Shirley', last_name='Kim', gender='F'),
]

session_maker = sessionmaker(bind=create_engine('sqlite///models.db'))

def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

create_users()

with session_maker() as session:
    user_records = session.query(UserModel).all()
    for user in user_records:
        print(user)
        
with session_maker() as session:
    user_records = session.query(UserModel).all
    for user in user_records:
        print(user.full_name)
        