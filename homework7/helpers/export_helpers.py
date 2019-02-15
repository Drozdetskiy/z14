import csv
import json
import pickle


class DataSetter:

    def __init__(self, input_path, output_path='', data=None):
        self.input_path = input_path
        self.output_path = output_path
        self.data = data

    def _export_to_json(self):
        _file = open(self.output_path, 'w')
        _file.write(json.dumps(self.data))
        _file.close()

    def _export_to_xml(self):
        file = open(self.output_path, 'w')
        items = ''
        for item in self.data:
            item_str = ''
            for key, value in item.items():
                item_str += f'<{key}>{value}</{key}>'
            items += f'<item>{item_str}</item>'
        result = f'<root>{items}</root>'
        file.write(result)
        file.close()

    def _export_to_csv(self):
        _file = open(self.output_path, 'w')
        writer = csv.DictWriter(_file, fieldnames=self.data[0])
        writer.writeheader()
        writer.writerows(self.data)
        _file.close()

    def _export_to_bin(self):
        _file = open(self.output_path, 'wb')
        pickle.dump(self.data, _file)
        _file.close()

    def _export_to_screen_print(self):
        return print(self.data)
