from openpyxl import Workbook


def addLine(line):
    #wb = Workbook()
    wb = openpyxl.load_workbook(balances.xlsx)
    print(wb)
    ws = wb.active
    print(ws)
    ws.append(line)
    wb.save('balances.xlsx')


if __name__ == '__main__':
    l1 = ['This is A1', 'This is B1', 'This is C1']
    l2 = ['This is A2', 'This is B2', 'This is C2']
    l3 = ['This is A3', 'This is B3', 'This is C3']
    addLine(l1)
