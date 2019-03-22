from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker
from models import User, Test, Question, Answer, TestContest, UsersAnswer


class InputError(Exception):
    pass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls
            ).__call__(*args, **kwargs)
        return cls._instances[cls]


def none_error_decorator(func):
    def _func(*args, **kwargs):
        if not func(*args, **kwargs):
            raise InputError
        return func(*args, **kwargs)
    return _func


class Homework13Gateway(metaclass=Singleton):
    def __init__(self):
        engine = create_engine(
            f'postgresql://{getenv("DB_USER")}:{getenv("DB_PASSWORD")}@'
            f'{getenv("DB_HOST")}:{getenv("DB_PORT")}/{getenv("DB_NAME")}'
        )
        self.engine = engine
        Session = sessionmaker(bind=engine)
        self.session = Session()

    @none_error_decorator
    def _query_test_id(self, test_name):
        return self.session.query(Test.id).\
            filter(Test.name == test_name).all()

    @none_error_decorator
    def _query_user_id(self, user_name):
        return self.session.query(User.id).\
            filter(User.name == user_name).all()

    @none_error_decorator
    def _query_test_questions(self, test_name):
        return self.session.query(Question.question_text).join(TestContest).\
            join(Test).filter(Test.name == test_name).all()

    @none_error_decorator
    def _query_questions_id(self, test_name):
        return [i[0] for i in self.session.query(TestContest.question).
                join(Test).filter(Test.name == test_name).all()]

    @none_error_decorator
    def _query_cases(self, question_number):
        return self.session.query(Answer.answer_text, Answer.id).\
            filter(Answer.question == question_number).all()

    def query_test(self, test_name_dict):
        _res = test_name_dict
        for index, question in enumerate(
                self._query_test_questions(test_name_dict['test_name'])
        ):
            _res[f'question {index + 1}'] = question[0]

        for id_num in self._query_questions_id(test_name_dict['test_name']):
            for index, case in enumerate(self._query_cases(id_num)):
                _res[f'case{id_num}-{index + 1}'] = case

        return _res

    def input_answers(self, answer):
        user_id = self._query_user_id(answer['user_name'])[0][0]
        test_id = self._query_test_id(answer['test_name'])[0][0]
        for i, q_id in enumerate(
                self._query_questions_id(answer['test_name'])):
            new_answer = UsersAnswer(
                user=user_id,
                test=test_id,
                question=q_id,
                answer=answer[f'question_{i + 1}']
            )
            self.session.add(new_answer)
        self.session.commit()

    def query_user_result(self, result_parameters):
        user_name = result_parameters['user_name']
        test_name = result_parameters['test_name']

        return self.session.query(
            User.name,
            Test.name,
            Question.question_text,
            Answer.trueness
        ).join(
            UsersAnswer,
            UsersAnswer.user == User.id and
            UsersAnswer.test == Test.id
        ).filter(User.name == user_name).\
            filter(Test.name == test_name).\
            join(Question).join(
            Answer,
            Answer.id == UsersAnswer.answer
        ).all()


if __name__ == '__main__':
    gt = Homework13Gateway()
    print(gt.query_user_result({'user_name': 'user1', 'test_name': 'test_1'}))
