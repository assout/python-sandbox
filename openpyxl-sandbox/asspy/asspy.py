#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :
import openpyxl

if __name__ == '__main__':
    """
    """
    wb = openpyxl.Workbook()

    # 保存
    wb.save('example.xlsx')
