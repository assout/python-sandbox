#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import openpyxl
from collections import namedtuple

import os
import shutil
import argparse
from dataclasses import dataclass
from copy import copy
from typing import NamedTuple


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

    # Data Classes
    @dataclass(frozen=True)
    class SourceRecord:
        id: int
        name: str
        is_oridinal: bool = False

        def bow(self) -> str:
            return self.name + ' めー'

    record = SourceRecord(1, "りんご")
    print(record.bow())
    print(record.name)

    # Data Classes
    @dataclass(frozen=True)
    class SourceRecord:
        """
        データ
        """
        id: int
        name: str
        is_oridinal: bool = False

        def bow(self) -> str:
            return self.name + ' めー'

    record = SourceRecord(1, "りんご")
    print(record.bow())
    print(record.name)

    # Named Tuple
    Item = namedtuple('Item', ('title', 'url', 'user', 'body'))
    i = Item(title='item1', url='http:example.com/item1', user='user1',
             body='body1')
    print(i.body)
    print(i.user)

    # Named Tuple2
    Item2 = NamedTuple('Item2', [('title', str), ('price', int)])
    i2 = Item2(title="hoge", price="fuga")
    print(i2.title)


if __name__ == '__main__':
    print(os.getcwd())
    main()
