import csv
import json
import pickle
import xml.etree.ElementTree as eTree

from os import path


def path_checker(method):
    def _method(self):
        return print(f'Path {self.input_path} doesn`t exist')\
            if not path.exists(self.input_path) else\
            method(self)
    return _method


class DataGetter:

    def __init__(self, input_path, output_path='', data=None):
        self.input_path = input_path
        self.output_path = output_path
        self.data = data

    @path_checker
    def _import_from_csv(self):
        self.data = []
        _file = open(self.input_path)
        _reader = csv.DictReader(_file)
        for line in _reader:
            self.data.append(dict(line))
        _file.close()

    @path_checker
    def _import_from_xml(self):
        self.data = []
        _raw_data = eTree.parse(self.input_path)
        root = _raw_data.getroot()
        for number, item in enumerate(root):
            if not len(item):
                self.data.append({item.tag: item.text})
            else:
                self.data.append({})
                for child in item.getchildren():
                    self.data[number][child.tag] = child.text

    @path_checker
    def _import_from_json(self):
        _file = open(self.input_path, 'r')
        json_data = _file.read()
        _file.close()
        self.data = json.loads(json_data)

    @path_checker
    def _import_from_bin(self):
        _file = open(self.input_path, 'rb')
        self.data = pickle.load(_file)
        _file.close()
