from openpyxl import Workbook
def test():
    wb = Workbook()
    print(wb)
    ws = wb.active
    print(ws)
    ws.append(['This is A1', 'This is B1', 'This is C1'])
    ws.append(['This is A2', 'This is B2', 'This is C2'])
    ws.append(['This is A3', 'This is B3', 'This is C3'])
    wb.save('balances.xlsx')
if __name__ == '__main__':
    test()