from sqlalchemy import create_engine, Integer, String, ForeignKey, select, Text, and_, desc, func
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship

engine = create_engine('sqlite:///:memory:', echo=False)  # noqa
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname: Mapped[str] = mapped_column(String)


class Post(Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[str] = mapped_column('user_id', Integer, ForeignKey('users.id'))
    user: Mapped['User'] = relationship(User)


Base.metadata.create_all(engine)

if __name__ == '__main__':
    names = ['Crystal Najera', 'Shaun Beck', 'Kathrin Reinhardt']
    for name in names:
        user = User(fullname=name)
        session.add(user)
    session.commit()

    # stmt = select(User)
    # result = session.execute(stmt)
    # for user in result.scalars():
    #     print(user.id, user.fullname)

    stmt = select(User.id, User.fullname)
    result = session.execute(stmt)
    users = []
    for row in result:
        print(row)
        users.append(row)

    for user in users:
        post = Post(title=f'Title {user[1]}', body=f'Body post user {user[1]}', user_id=user[0])
        session.add(post)
    session.commit()

    # stmt = select(User).where(User.fullname == "Shaun Beck")
    # result = session.execute(stmt).scalar_one()
    # print(result.id, result.fullname)
    print('---------------------')
    stmt = select(User).where(User.fullname.like("%ha%"))
    result = session.execute(stmt)

    for user in result.scalars().all():
        print(user.id, user.fullname)
    print('---------------------')
    stmt = select(User).where(User.fullname.like("%ha%")).where(User.fullname != 'Shaun Beck')
    result = session.execute(stmt)

    for user in result.scalars().all():
        print(user.id, user.fullname)
    print('---------------------')
    stmt = select(User).where(and_(User.fullname.like("%ha%"), User.fullname != 'Shaun Beck'))
    result = session.execute(stmt)

    for user in result.scalars():
        print(user.id, user.fullname)
    print('---------------------')
    stmt = select(User).order_by(User.fullname)
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)
    print('---------------------')
    stmt = select(User).order_by(desc(User.fullname))
    result = session.execute(stmt)
    for user in result.scalars():
        print(user.id, user.fullname)
    print('---------------------')
    stmt = (
        select(User.fullname, func.count(Post.id))  # создаем объект select с выборкой имени пользователя и количества постов
        .join(Post)  # делаем join с моделью Post по внешнему ключу user_id
        .group_by(User.fullname)  # группируем результаты по имени пользователя
    )
    results = session.execute(stmt).all()  # выполняем запрос и получаем список кортежей
    for name, count in results:  # перебираем результаты
        print(f"{name} has {count} posts")  # выводим имя пользователя и количество постов
