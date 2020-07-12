from pprint import pprint
import datetime
import argparse
from stock.single_stock import ConstStock
from stock.single_stock import Stock
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
            self.add_stock()
        dall = self.db.get_all()
        pprint(dall)

    def add_stock(self):
        """
        start with prompt/select manually
        """
        d = {}
        dall = self.get_all()

        from stock.single_stock import ConstStock
        st = ConstStock()
        for key in st.keys():
            # value = raw_input('Please type value for {}'.format(key))
            value = input('{} is: '.format(key))

            if not value:
                value = 'NA'

            if key == 'name':
                print('find stock name')
                dstock = dall.get(value, {})
                if dstock:
                    print('found stock, add become update')
                    pprint(dstock)
                    return self.update_stock(value, dstock)

            d[key] = value
        dnew = self.new_entry(d)
        self.log_append(dnew)

    def new_entry(self, dstock):
        """
        make it a nested dict with variable length to test
        """
        # exchange/name/reviewid(datetimestr)/review=jsonstr/userid
        dt = datetime.datetime.now()
        reviewid = dt.isoformat()
        userid = 'user'
        s = Stock(**dstock)
        # reord -- initial setup a stock
        # reviewid -- with updated info, another class Event?

        dev = {reviewid: dstock, 'user': userid}
        pprint(dev)

        d = {s.stock.name: {s.stock.exchange: {'review': dev}}}
        return d

    def updated_entry(self, name, dold, dstock):
        """
        make it a nested dict with variable length to test
        dold without name
        """
        # exchange/name/reviewid(datetimestr)/review=jsonstr/userid
        dt = datetime.datetime.now()
        reviewid = dt.isoformat()
        userid = 'user'
        keys = list(dold.keys())

        # exchange might be one, but could be more
        # to be refactored
        # using select_from

        exchange = keys[0]

        dev = dold.get(exchange, {})

        # part to be updated
        dreview = dev.get('review', {})

        import copy
        dnew = copy.deepcopy(dreview)
        review = {reviewid: dstock, 'user': userid}
        dnew.update(review)

        # add dnew to be new review
        # add new entry
        # d = {name: {exchange: {'review': dnew}}}

        # d = self.nested.update(dold, dnew)
        keys = [name, exchange, 'review']
        d = self.nested.set(dold, keys, dnew)
        return d

    def choose_exchange(self, key):
        pass

    def update_stock(self, name, d):
        """
        review with new price/dividend/more info
        """
        dnew = {}
        for key in self.keys_update():
            print(key)
            value = input('Value for {} is: '.format(key))
            if not value:
                value = 'NA'
            dnew[key] = value
        dline = self.updated_entry(name, d, dnew)
        self.log_append(dline)
