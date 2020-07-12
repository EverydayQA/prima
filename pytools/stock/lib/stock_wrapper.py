from pprint import pprint
import datetime
import argparse
from lib.single_stock import ConstStock
from lib.single_stock import Stock


class StockWrapper(ConstStock):

    def __init__(self, *args, **kwargs):
        # only args input, the rest goes to each func
        self.args = args
        self.kwargs = kwargs
        self.ns = argparse.Namespace(**kwargs)

    def show(self):
        self.log_stock()
        self.todo()

    def action(self):
        if self.ns.add:
            self.add_stock()
        dall = self.get_all()
        pprint(dall)

    def add_stock(self):
        """
        start with prompt/select manually
        """
        d = {}
        dall = self.get_all()

        from lib.single_stock import ConstStock
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
        # exchange/name/eventid(datetimestr)/event=jsonstr/userid
        dt = datetime.datetime.now()
        eventid = dt.isoformat()
        userid = 'user'
        s = Stock(**dstock)
        # reord -- initial setup a stock
        # eventid -- with updated info, another class Event?

        dev = {eventid: dstock, 'user': userid}
        pprint(dev)

        d = {s.stock.name: {s.stock.exchange: {'event': dev}}}
        return d

    def updated_entry(self, name, dold, dnew):
        """
        make it a nested dict with variable length to test
        dold without name
        """
        # exchange/name/eventid(datetimestr)/event=jsonstr/userid
        dt = datetime.datetime.now()
        eventid = dt.isoformat()
        userid = 'user'
        keys = list(dold.keys())
        exchange = keys[0]
        dev = dold.get(exchange, {})
        devent = dev.get('event', {})

        import copy
        devent_new = copy.deepcopy(devent)
        event = {eventid: dnew, 'user': userid}
        devent_new.update(event)

        # add dnew to be new event
        # add new entry
        d = {name: {exchange: {'event': devent_new}}}
        return d

    def choose_exchange(self, key):
        pass

    def update_stock(self, name, d):
        """
        event with new price/dividend/more info
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
