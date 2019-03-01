import unittest
import json
import xml
import pickle
from my_homework6 import parse_json, \
    parse_xml, \
    parse_csv, \
    parse_bin, \
    dump_json, \
    dump_csv, \
    dump_bin, \
    dump_xml, \
    main, \
    get_extension


class ParseJsonTest(unittest.TestCase):
    def test_parse_json(self):
        self.assertEqual(parse_json('testdata.json'),
                         {"1": "11", "2": "22", "3": "33"})

    def test_parse_exc(self):
        with self.assertRaises(json.decoder.JSONDecodeError):
            parse_json('testdata_exc.json')


class ParseXmlTest(unittest.TestCase):
    def test_parse_xml(self):
        self.assertEqual(parse_xml('testdata.xml'),
                         [{},
                          {'author': '1', 'description': '2'},
                          {'publish_date': '1', 'description': '2'}]
                         )

    def test_parse_exc(self):
        with self.assertRaises(xml.etree.ElementTree.ParseError):
            parse_xml('testdata_exc.xml')


class ParseCsvTest(unittest.TestCase):
    def test_parse_csv(self):
        self.assertEqual(parse_csv('testdata.csv'),
                         [{'column1': 'name1',
                           'column2': 'surname1',
                           'column3': 'year1'},
                          {'column1': 'name2',
                           'column2': 'surname2',
                           'column3': 'year2'}]
                         )


class ParseBinTest(unittest.TestCase):
    def test_parse_bin(self):
        self.assertEqual(parse_bin('testdata.bin'),
                         {'1': '11', '2': '22', '3': '33'})

    def test_parse_exc(self):
        with self.assertRaises(pickle.UnpicklingError):
            parse_bin('testdata_exc.bin')


class DumpTest(unittest.TestCase):
    def test_dump_csv(self):
        data = [{'column1': 'name1',
                 'column2': 'surname1',
                 'column3': 'year1'},
                {'column1': 'name2',
                 'column2': 'surname2',
                 'column3': 'year2'}
                ]
        dump_csv('testfuncres.csv', data)
        str_1 = str(self.read_file('testfuncres.csv'))
        str_2 = str(self.read_file('testres.csv'))
        self.assertMultiLineEqual(str_1, str_2)

    def test_dump_json(self):
        data = {"1": "11", "2": "22", "3": "33"}
        dump_json('testfuncres.json', data)
        str_1 = str(self.read_file('testfuncres.json'))
        str_2 = str(self.read_file('testres.json'))
        self.assertMultiLineEqual(str_1, str_2)

    def test_dump_xml(self):
        data = [{},
                {'author': '1', 'description': '2'},
                {'publish_date': '1', 'description': '2'}
                ]
        dump_xml('testfuncres.xml', data)
        str_1 = str(self.read_file('testfuncres.xml'))
        str_2 = str(self.read_file('testres.xml'))
        self.assertMultiLineEqual(str_1, str_2)

    def test_dump_bin(self):
        data = {'1': '11', '2': '22', '3': '33'}
        dump_bin('testfuncres.bin', data)
        str_1 = str(self.read_file('testfuncres.bin'))
        str_2 = str(self.read_file('testres.bin'))
        self.assertMultiLineEqual(str_1, str_2)

    @staticmethod
    def read_file(file_name):
        with open(file_name, 'rb') as file:
            return file.readlines()


class MainTest(unittest.TestCase):
    def test_bad_args(self):
        self.assertIsNone(main(''))


class GetExtensionTest(unittest.TestCase):
    def test_right_extension(self):
        for ext in ('bin', 'csv', 'xml', 'json'):
            self.assertEqual(get_extension(f'test.{ext}'), ext)

    def test_no_extension(self):
        self.assertIsNone(get_extension(None))


if __name__ == '__main__':
    unittest.main()
