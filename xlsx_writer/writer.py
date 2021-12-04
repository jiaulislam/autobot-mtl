from typing import List, Tuple
from xlsxwriter import Workbook
from xlsxwriter.worksheet import Worksheet


class SheetWrapper:

    headers: List[str] = [
                'SL NO',
                'Date',
                'Project Coordinator',
                'Project Name',
                'Change Activity',
                'Impact List',
                'Service Type',
                'Downtime',
                'Commercial Zone',
                'NCR Number',
                'Change Manager',
                'Current Status'
    ]



class Writer:
    __db_data_length = 1

    def __init__(self, file_name: str, sheet_name: str='Main'):
        self.file_name = file_name
        self.workbook = Workbook(file_name)
        self.worksheet: Worksheet = self.workbook.add_worksheet(sheet_name)
        self.__date_format = self.workbook.add_format({'num_format': 'dd-mmm-yyyy'})

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def write_to_excel(self, _db_data: List[Tuple]) -> None:
        self.__db_data_length += self.get_data_length(_db_data)

        for _row in range(1,len(_db_data)+1):
            for _idx, _col in enumerate(_db_data[_row-1]):
                if _idx == 0:
                    self.worksheet.write_number(_row, _idx, _row)
                elif _idx == 1:
                    self.worksheet.write_datetime(_row, _idx, _col, self.__date_format)
                elif _idx == 12:
                    # no need to give user created_at value
                    pass
                else:
                    self.worksheet.write_string(_row, _idx, str(_col))
        self.__make_table()


    @staticmethod
    def get_data_length(data: list[tuple]) -> int:
        return len(data)

    def __make_table(self):
        _options = {
            'style': 'Table Style Light 17',
            'columns': [{'header': i.upper()} for i in SheetWrapper.headers]
        }
        self.worksheet.add_table(f'A1:L{self.__db_data_length}', options=_options)

    def close(self):
        self.workbook.close()