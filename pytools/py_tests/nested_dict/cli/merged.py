from pprint import pprint
from src.dict_merge import DictMerge


class ConstDemo(object):

    def demo_one(self):
        # test const
        from const.first_const import ConstCourse
        ConstCourse.ENGLISH = 'french'
        const = ConstCourse()
        print(const.ENGLISH)
        const.ENGLISH = 'english'
        print(const.ENGLISH)

    def demo_two(self):
        from const.second_const import _Const
        print(_Const.FOO)
        _Const.FOO = 'bar'
        print(_Const.FOO)
        const = _Const()
        print(const.FOO)
        const.FOO = 'barr'
        print(const.FOO)

    def get_datetime(self):
        import datetime
        dt = datetime.datetime.strptime('2011-11-12', '%Y-%m-%d')
        print(dt)
        print(type(dt))
        return dt

    def d_cour(self, courses):
        d = {}
        for cour in courses:
            items = self.get_prefix_suffix(cour)
            prefix = items[0]
            suffix = items[1]
            dpre = d.get(prefix, {})
            dpre.update({suffix: cour})
            d[prefix] = dpre
        print(d)
        return d

    def get_prefix_suffix(self, string):
        chars = list(string)
        items_d = []
        index = len(chars)
        for char in reversed(chars):
            if char.isdigit() is False:
                break
            else:
                items_d.append(char)
            index = index - 1
        suffix = ''.join(reversed(items_d))
        prefix = ''.join(chars[0:index])
        print('prefix {} suffix {}'.format(prefix, suffix))
        return [prefix, suffix]

    def cli_do(self):
        self.get_datetime()
        self.get_prefix_suffix('eng003')
        self.d_cour(['fench001', 'latin', 'eng002', 'eng005', 'eng10'])


def main():
    print('merge of a dict')
    adict = {'key1': 1, 'key2': 2, 'key3': 3}
    ds = DictMerge(**adict)
    d2 = {'Ritika': 5, 'Sam': 7, 'John': 10}
    d = ds.merge(d2)
    pprint(d)
    ds.demo()
    dem = ConstDemo()
    # dem.demo_one()
    dem.cli_do()

    from const import course
    print(course.FRENCH)
    # these is nothing prevent it being changed
    course.FRENCH = 'anglais'
    print(course.FRENCH)


if __name__ == "__main__":
    main()
