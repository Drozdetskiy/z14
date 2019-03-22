"""
Программа на вход принимает название мода и данные, соответствующие моду.
Список модов:
1. input_answers {'user_name':'user1','test_name':'test_1','question_1':2,'question_2':2,'question_3':1}


2. query_test {'test_name':<test_name>}

3. query_user_result {'user_name':<user_name>,'test_name':<test_name>}

"""


import sys
import gateway
import ast


def main(args):
    gt = gateway.Homework13Gateway()
    return getattr(gt, args[1])(ast.literal_eval(args[2]))


if __name__ == '__main__':
    main(sys.argv)
