

class AStock(object):
    """
    quick put stock name and exchange in to a file(db)
    """
    ETF = 'ETF'
    STX = 'STX'
    NYSE = 'NYSE'

    def __init__(self, *args, **kwargs):
        pass

    def exchanges(self):
        return [STX, NYSE]

    def types(self):
        return ['REIT','ETF', 'INDEX']

    def categories(self):
        return ['bank', 'finance', 'oil', 'food', 'agriculture', 'hightech', 'weapon', 'travel', 'machinary', 'engine', 'pharceutical', 'realestate', 'media', 'ET', 'chip']

    def prompt(self, stock):
        items = ['name', 'desc', 'exchange', 'dividend','country', 'industry', 'like', 'type'] 
        return items

