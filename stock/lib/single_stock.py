

class Exchange(object):
    STX = 'STX'
    NYSE = 'NYSE'


class Stock(object):

    def dividend(self):
        pass

    def volume(self):
        pass

    def description(self):
        pass

    def std_name(self):
        """
        TD for TD bank e.g
        """
        return 'std'

    def long_name(self):
        pass

    def exchange(self):
        pass

    def category(self):
        """
        oil/manufacture/edu/pharmaceutical/food/bank/financial/
        """
        pass

    def score(self):
        pass

    def value(self):
        pass

    def buy_at(self):
        pass

    def sell_at(self):
        pass

