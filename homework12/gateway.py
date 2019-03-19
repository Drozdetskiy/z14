import psycopg2


class InputError(Exception):
    pass


def none_error_decorator(func):
    def _func(*args, **kwargs):
        if not func(*args, **kwargs):
            raise InputError
        return func(*args, **kwargs)
    return _func


class Homework12Gateway:
    def __init__(self):
        self.connection = psycopg2.connect(
            dsn='postgres://z14:3778952@localhost:5432/homework_12'
        )

        self.cursor = self.connection.cursor()

    @none_error_decorator
    def _query_test_id(self, test_name):
        self.cursor.execute(f"SELECT test.id "
                            f"FROM test "
                            f"WHERE test.name = '{test_name}'"
                            )
        _res = self.cursor.fetchall()
        if not _res:
            raise InputError
        return _res

    @none_error_decorator
    def _query_user_id(self, user_name):
        self.cursor.execute(f"SELECT users.id "
                            f"FROM users "
                            f"WHERE users.name = '{user_name}'"
                            )

        return self.cursor.fetchall()

    @none_error_decorator
    def _query_test_questions(self, test_name):
        self.cursor.execute(f"SELECT questions.question_contest "
                            f"FROM test JOIN test_contest "
                            f"ON (test_contest.test_id = test.id) "
                            f"JOIN questions "
                            f"ON (test_contest.question_id = questions.id) "
                            f"WHERE test.name = '{test_name}'"
                            )

        return self.cursor.fetchall()

    @none_error_decorator
    def _query_questions_id(self, test_name):
        self.cursor.execute(f"SELECT test_contest.question_id "
                            f"FROM test_contest JOIN test "
                            f"ON (test_contest.test_id = test.id) "
                            f"WHERE test.name = '{test_name}'"
                            )

        return [i[0] for i in self.cursor.fetchall()]

    @none_error_decorator
    def _query_cases(self, question_number):
        self.cursor.execute(f"SELECT cases.case_text, cases.id "
                            f"FROM cases "
                            f"WHERE cases.question_id = {question_number}"
                            )

        return self.cursor.fetchall()

    def query_test(self, test_name_dict):
        _res = test_name_dict
        for index, question in enumerate(
                self._query_test_questions(test_name_dict['test_name'])
        ):
            _res[f'question {index + 1}'] = question[0]

        for id in self._query_questions_id(test_name_dict['test_name']):
            for index, case in enumerate(self._query_cases(id)):
                _res[f'case{id}-{index + 1}'] = case

        print(_res)

    def input_answers(self, answer):
        user_id = self._query_user_id(answer['user_name'])[0][0]
        test_id = self._query_test_id(answer['test_name'])[0][0]
        _str = ','.join(
            ('({}, {}, {}, {})'.format(
                user_id,
                test_id,
                q_id,
                answer[f'question_{i + 1}']
                )
                for i, q_id in enumerate(
                self._query_questions_id(answer['test_name'])
            )
            )
        )

        self.cursor.execute(
            f"INSERT INTO users_answers ("
            f"user_id, "
            f"test_id, "
            f" question_id,"
            f" case_id)"
            f" VALUES {_str};"
        )

        self.connection.commit()

    def query_user_result(self, result_parameters):
        user_name = result_parameters['user_name']
        test_name = result_parameters['test_name']

        self.cursor.execute(f"SELECT users.name, "
                            f"test.name, "
                            f"questions.question_contest, cases.trueness "
                            f"FROM users_answers JOIN users "
                            f"ON (users_answers.user_id = users.id) "
                            f"JOIN test "
                            f"ON (users_answers.test_id = test.id) "
                            f"JOIN questions "
                            f"ON (users_answers.question_id = questions.id) "
                            f"JOIN cases "
                            f"ON (users_answers.case_id = cases.id) "
                            f"WHERE test.name = '{test_name}' "
                            f"AND users.name = '{user_name}'"
                            )

        print(self.cursor.fetchall())
