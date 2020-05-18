from connetct import Base
from datetime import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(12))
    password = Column(String(20))
    creatime = Column(DateTime, default=datetime.now)
    _locked = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return """
        <User(id:%s, username:%s, password:%s, creatime:%s)>
        """ % (self.id,
               self.username,
               self.password,
               self.creatime
               )


class UserDetails(Base):
    __tablename__ = 'user_details'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_card = Column(Integer, nullable=True, unique=True)
    last_login = Column(DateTime, default=datetime.now)
    login_num = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))
    userdetail = relationship('User', backref='details', uselist=False, cascade='all')

    def __repr__(self):
        return """
        <User(id:%s, id_card:%s, last_login:%s, login_num:%s, user_id:%s, userdetail:%s)>
        """ % (self.id,
               self.id_card,
               self.last_login,
               self.login_num,
               self.user_id,
               self.userdetail,
               )


if __name__ == '__main__':
    Base.metadata.create_all()