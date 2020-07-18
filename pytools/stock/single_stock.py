

class Exchange(object):
    TSX = 'TSX'
    NYSE = 'NYSE'

    def exchanges(self):
        return [self.stx, self.NYSE]

    def d_unit(self):
        d = {}
        d[self.TSX] = 'CAD'
        d[self.NYSE] = 'USD'


class ConstStock(Exchange):
    DIVIDEND = 'dividend'
    VOLUME = 'volume'
    DESCRIPTION = 'description'
    # TD for TD bank e.g
    NAME = 'name'
    # oil/manufacture/edu/pharmaceutical/food/bank/financial/
    FIELD = 'field'
    LONGNAME = 'longname'
    EXCHANGE = 'exchange'
    SCORE = 'score'
    PRICE = 'price'
    ORIGIN = 'origin'

    def keys(self):
        return [self.NAME, self.EXCHANGE, self.LONGNAME, self.FIELD, self.ORIGIN, self.DESCRIPTION]

    def keys_review(self):
        return [self.PRICE, self.DIVIDEND, self.SCORE, self.DESCRIPTION]


class Stock(ConstStock):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def is_valid_exchange(self, value):
        if not value:
            return False
        if value in self.exchanges():
            return True
        return False

    def todo(self):
        print('input validation -- this class')
