#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import openpyxl
import shutil
import argparse
from dataclasses import dataclass


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

    shutil.copyfile("./template.xlsx", "new.xlsx")
    wb = openpyxl.load_workbook('new.xlsx')
    ws = wb["Sheet"]
    print(ws)
    print(tuple(ws))
    # s['A1:']

    # i = openpyxl.utils.cell.column_index_from_string("b")
    # print(i)

    record = SourceRecord(1, "りんご")
    print(record.bow())


if __name__ == '__main__':
    main()
