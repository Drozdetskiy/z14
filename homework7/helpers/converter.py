import re

from import_helpers import DataGetter
from export_helpers import DataSetter


class DataConverter(DataGetter, DataSetter):

    def convert(self):
        _extension_1 = self.define_extension(self.input_path)
        _extension_2 = self.define_extension(self.output_path)
        getattr(self, f'_import_from_{_extension_1}', self.wrong_extension)()
        if self.data:
            getattr(self,
                    f'_export_to_{_extension_2}',
                    self.wrong_extension)()

    @staticmethod
    def define_extension(_path):
        m = re.search(r'(?<=\.)(\w+)', _path)
        return m.group(0) if m else 'screen_print'

    @staticmethod
    def wrong_extension():
        print('Extension doesn`t supply')
