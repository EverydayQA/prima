from pprint import pprint
import datetime
import argparse
from stock.single_stock import ConstStock
# from stock.single_stock import Stock
from stock.stock_log import StockLog
from nested_dict.nested_dict import NestedDict


class StockWrapper(ConstStock):

    def __init__(self, *args, **kwargs):
        # only args input, the rest goes to each func
        self.args = args
        self.kwargs = kwargs
        self.ns = argparse.Namespace(**kwargs)
        self.db = StockLog()
        self.nested = NestedDict()

    def show(self):
        self.db.log_stock()
        self.todo()

    def action(self):
        if self.ns.add:
            return self.add_stock()
        print('not --add')
        pprint(self.ns)

    def get_exchange(self, dex):
        from utils import menu
        exchanges = list(dex.keys())
        sels = menu.Menu().select_from_menu(exchanges, 'which Exchange?')
        if sels:
            if len(sels) > 1:
                print(sels)
                raise Exception('more than 1 exchange selected')
        return sels[0]

    def add_stock(self):
        """
        start with prompt/select manually
        """
        d = {}
        dall = self.db.get_all()

        from stock.single_stock import ConstStock
        st = ConstStock()
        for key in st.keys():
            # value = raw_input('Please type value for {}'.format(key))
            value = input('{} is: '.format(key))

            if not value:
                value = 'NA'

            if key == 'name':
                name = value
                print('find stock name')
                dex = dall.get(value, {})
                if dex:
                    exchange = self.get_exchange(dex)
                    print('found stock, add become update')
                    return self.update_stock(name, exchange)

            d[key] = value
        dnew = self.new_entry(d)
        self.db.log_append(dnew)

    def new_entry(self, dstock):
        """
        make it a nested dict with variable length to test
        """
        # exchange/name/reviewid(datetimestr)/review=jsonstr/userid
        dt = datetime.datetime.now()
        reviewid = dt.isoformat()
        userid = 'user'
        # reord -- initial setup a stock
        # reviewid -- with updated info, another class Event?
        s = argparse.Namespace(**dstock)
        dev = {reviewid: dstock, 'user': userid}
        pprint(dev)

        d = {s.name: {s.exchange: {'review': dev}}}
        return d

    def updated_entry(self, name, exchange, dold, dreview):
        """
        make it a nested dict with variable length to test
        dold without name
        """
        # exchange/name/reviewid(datetimestr)/review=jsonstr/userid
        dt = datetime.datetime.now()
        reviewid = dt.isoformat()
        userid = 'user'

        keys = [exchange, 'review']
        drev = self.nested.get(dold, keys)

        if not drev:
            print(name)
            print(exchange)
            pprint(dold)
            pprint(keys)
            print(drev)
            pprint(dreview)
            raise Exception('dnew None')

        import copy
        dnew = copy.deepcopy(drev)

        # single review
        review = {reviewid: dreview, 'user': userid}
        dnew.update(review)

        # add dnew to be new review
        # add new entry
        # d = {name: {exchange: {'review': dnew}}}

        # d = self.nested.update(dold, dnew)
        keys = [exchange, 'review']

        pprint(dnew)
        pprint(dold)
        # dcopy will be udpated
        dcopy = copy.deepcopy(dold)
        d = self.nested.set(keys, dnew, **dcopy)
        return {name: d}

    def update_stock(self, name, exchange):
        """
        review with new price/dividend/more info
        """
        # get exchane first
        # prompt or select
        dall = self.db.get_all()

        # for name
        d = dall.get(name, {})

        dnew = {}
        for key in self.keys_review():
            print(key)
            value = input('Value for {} is: '.format(key))
            if not value:
                value = 'NA'
            dnew[key] = value

        # updated entry for name
        dline = self.updated_entry(name, exchange, d, dnew)
        print('dline')
        pprint(dline)
        print('dline end')
        # self.db.log_append(dline)
