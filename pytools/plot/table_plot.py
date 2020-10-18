

class TablePlot(object):
    """
    which package installed and to be used
    screning_len/field length control?
    """

    def __init__(self):
        self.result = self.result1()

    def result1(self):
        lst = []
        lst.append(['desc', 'state'])
        lst.append(['eng', '60'])
        lst.append(['french', '33'])
        return lst

    def plot_tableit(self):
        try:
            import TableIt
        except Exception as e:
            print(e)
            return
        TableIt.printTable(self.result, useFieldNames=True)

    def plot_tabulate(self):
        try:
            from tabulate import tabulate
        except Exception as e:
            print(e)
            return
        print(tabulate(self.result))

    def plot_pretty(self):
        try:
            from prettytable import PrettyTable
        except Exception as e:
            print(e)
            return
        t = PrettyTable(['c1', 'c2'])
        for row in self.result:
            t.add_row(row)
        print(t)

    def plot_text(self):
        try:
            from texttable import TextTable
        except Exception as e:
            print(e)
            return
        t = TextTable()
        t.add_rows(self.result)
        print(t.draw())

    def plot_term(self):
        try:
            import termtables
        except Exception as e:
            print(e)
            return
        string = termtables.to_string(self.result)
        print(string)


def main():
    tp = TablePlot()
    tp.plot_term()
    tp.plot_text()
    tp.plot_pretty()
    tp.plot_tableit()
    tp.plot_tabulate()


if __name__ == '__main__':
    main()
