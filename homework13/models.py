from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, UniqueConstraint

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=100), unique=True)


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_text = Column(String(250))


class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    question = Column(ForeignKey(Question.id))
    answer_text = Column(String(250))
    trueness = Column(Boolean)


class Test(Base):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)


class TestContest(Base):
    __tablename__ = 'testcontests'
    id = Column(Integer, primary_key=True)
    test = Column(ForeignKey(Test.id))
    question = Column(ForeignKey(Question.id))
    __table_args__ = (
        UniqueConstraint('test', 'question', name='_question_test_uc'),
    )


class UsersAnswer(Base):
    __tablename__ = 'usersanswers'
    id = Column(Integer, primary_key=True)
    user = Column(ForeignKey(User.id))
    test = Column(ForeignKey(Test.id))
    question = Column(ForeignKey(Question.id))
    answer = Column(ForeignKey(Answer.id))
    __table_args__ = (
        UniqueConstraint(
            'user',
            'test',
            'question',
            'answer',
            name='_user_test_question_answer_uc'
        ),
    )


def create_tables():

    engine = create_engine(
        f'postgresql://{getenv("DB_USER")}:{getenv("DB_PASSWORD")}@'
        f'{getenv("DB_HOST")}:{getenv("DB_PORT")}/{getenv("DB_NAME")}'
    )
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_tables()
