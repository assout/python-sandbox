#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import openpyxl
import os
import shutil
import argparse
from dataclasses import dataclass
from copy import copy


@dataclass(frozen=True)
class SourceRecord:
    id: int
    name: str
    is_oridinal: bool = False

    def bow(self) -> str:
        return self.name + ' めー'


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    print(args.input)

    dest_name = "new.xlsx"
    shutil.copyfile("template.xlsx", dest_name)
    wb = openpyxl.load_workbook(dest_name)
    ws = wb["Sheet"]
    print(ws)
    for row in ws.iter_rows(min_row=2, min_col=1):
        for col in row:
            col._style = copy(col.offset(-1, 0)._style)

    ws.print_area.clear()
    wb.save(dest_name)
    # s['A1:']

    # i = openpyxl.utils.cell.column_index_from_string("b")
    # print(i)

    record = SourceRecord(1, "りんご")
    print(record.bow())


if __name__ == '__main__':
    print(os.getcwd())
    main()
