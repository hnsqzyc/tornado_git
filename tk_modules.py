from data.connetct import session
from data.user_modules import User, UserDetails


def add_user():
    person = User(username='敏敏', password='123')
    # session.add(person)
    #
    # persons = [
    #     User(username='颖颖', password='123'),
    #     User(username='丹丹', password='123'),
    #     User(username='周周', password='123'),
    # ]
    # persons = [
    #     UserDetails(id_card=411425190),
    #     UserDetails(id_card=411425191),
    #     UserDetails(id_card=411425192),
    #     UserDetails(id_card=411425193),
    # ]
    # session.add_all(persons)
    # session.commit()


def search_user():
    # rows = session.query(User).get(2)
    # print(rows.username)
    # print(rows)
    # print(rows.details[0])
    # print('*' * 30)
    # row = session.query(UserDetails).get(2)
    # print(row)
    # 多表查询
    # print(session.query(UserDetails, User).all())  # 这个是 cross join
    # print(session.query(UserDetails, User).filter(User.id == UserDetails.id).all())  # 这是也是cross join 但是加上了where条件
    #
    # print(session.query(User.username, UserDetails.last_login).join(UserDetails,
    #                                                                 UserDetails.id == User.id).all())  # 这个是inner join
    #
    # print(session.query(User.username, UserDetails.last_login).outerjoin(UserDetails,
    #                                                                      UserDetails.id == User.id).all())  # 这个才是左连接，sqlalchemy没有右连接
    #
    q1 = session.query(User.id)
    q2 = session.query(UserDetails.id)
    print(q1.union(q2).all())  # 这个是union关联


def update_user():
    rows = session.query(User).filter(User.username == '敏敏').update({User.password: 456})
    session.commit()


def delete_user():
    rows = session.query(User).filter(User.username == '敏敏')[0]
    print(rows)
    session.delete(rows)
    session.commit()


if __name__ == '__main__':
    # add_user()
    search_user()
    # update_user()
    # delete_user()