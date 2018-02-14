import unittest
import re


class TestMatch(unittest.TestCase):

    def test_match1(self):
        """
        (?:a{6})* matches any multiple of six 'a' characters.
        (?:...)
        A non-capturing version of regular parentheses.
        Matches whatever regular expression is inside the parentheses,
        but the substring matched by the group cannot be retrieved after performing a match or referenced later in the pattern.
        """
        line = 'test_aaaaaaaa_bb_cc_ggaaaaaaa.txt'
        re.findall('(?:a{6})*', line)
        # self.assertEquals(items, line)

    def test_match2(self):
        """
        Raw string notation (r"text") keeps regular expressions sane.
        Causes the resulting RE to match 1 or more repetitions of the preceding RE.
        # ab+ will match a followed by any non-zero number of b s; it will not match just a
        """
        text = "He was carefully disguised but captured quickly by police."
        items = re.findall(r"\w+ly", text)
        self.assertEquals(items, ['carefully', 'quickly'])

    def test_findall_2(self):
        line = 'June 24, August 9, Dec 12'

        regex = r"[a-zA-Z]+ \d+"
        matches = re.findall(regex, line)
        self.assertEquals(matches, ['June 24', 'August 9', 'Dec 12'])

        regex = r"([a-zA-Z]+) \d+"
        matches = re.findall(regex, line)
        self.assertEquals(matches, ['June', 'August', 'Dec'])

        line = 'test_mm_ff_ss_mmm.txt'
        regex = r"(.+?)_+"
        matches = re.findall(regex, line)
        self.assertEquals(matches, ['test', 'mm', 'ff', 'ss'])

        regex = r"(.+?)_+"
        #
        line = 'test_m_m_ff_ss__mmm.txt'
        matches = re.findall(regex, line)
        self.assertEquals(matches, ['test', 'm', 'm', 'ff', 'ss'])

        # split should be enough
        # items.pop(0)
        # items[0] or 0 1 match mm, then pop(0 or 01)
        # ff items[0] pop(0)
        # ss items[0]
        matches = re.split('_+', line)
        self.assertEquals(matches, ['test', 'm', 'm', 'ff', 'ss', 'mmm.txt'])

        line = 'abc="abc";\n"bbb\\n",\n"ccc\\n",\n"ddd";\neee="eee";\n'
        items = re.split(';\n', line)
        self.assertEqual(items, [])
        s = "2**3 + 2*3"
        items = re.findall(r'[+*-/()]+|\d+', s)
        self.assertEqual(items, ['2', '**', '3', '+', '2', '*', '3'])
        string = 'blah blah 12234 (12) (23) (34)'
        items = re.findall(r'\((\d+)+\)', string)
        self.assertEqual(items, ['12', '23', '34'])
        # Use a postive lookbehind and look-ahead in your regex,
        items = re.findall(r'(?<=\()\d+(?=\))', string)
        self.assertEqual(items, ['12', '23', '34'])
        string = '<dirtfields name="one" value="stuff">\n<gibberish name="two"\nwewt>'
        items = re.findall(r'name="([^"]*)"', string, re.IGNORECASE)
        self.assertEqual(items, ['one', 'two'])
        items = re.findall(r'(?<=name=")[^"]*', string, re.IGNORECASE)
        self.assertEqual(items, ['one', 'two'])
        items = re.findall(r'(?<=name=")[^"]*(?=")', string, re.IGNORECASE)
        self.assertEqual(items, ['one', 'two'])
        # [m.groupdict() for m in regex.finditer(search_string)]

    def test_date_time(self):
        line = 'Today is 2018-02-10.'
        regex = '(?P<year>(?:19|20)\d\d)(?P<delimiter>[- /.])(?P<month>0[1-9]|1[012])\2(?P<day>0[1-9]|[12][0-9]|3[01])'
        items = re.findall(regex, line)
        self.assertEqual(items, [])

    def test_ip(self):
        regex = '((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))'
        line = '192.168.0.2\n this is another line 199.243.255.34'
        items = re.findall(regex, line)
        self.assertEqual(items, ['192.168.0.2', '199.243.255.34'])

    def test_typho_chars(self):
        regex = '[^~\x22]+'
        line = '~sth~.txt'
        match = re.findall(regex, line)
        self.assertEqual(match, [])

    def test_split(self):
        regex = '(.*?) # .*'
        line = 'sth = sth # comment\n\n qwe = 234 # xxx\n'
        items = re.findall(regex, line)
        self.assertEqual(items, ['sth = sth', ' qwe = 234'])

    def test_none_capture(self):
        line = '<h1>aaa</h1>\n<h1>bbb</h1>'
        reg = '(?:<h1>)(.+?)(?:<\/h1>)'
        items = re.findall(reg, line)
        self.assertEqual(items, ['aaa', 'bbb'])

    def test_numbers(self):
        reg = '^(-?\d+)(\.\d+)?'
        items = re.findall(reg, '1.23')
        self.assertEqual(items, [])

        reg = '^[0-9]*$'
        line = '1234'
        items = re.findall(reg, line)
        self.assertEquals(items, [1234])
        # n digits number
        reg = '^\d{4}$'
        line = '12345'
        items = re.findall(reg, line)
        self.assertEquals(items, [1234])
        # at least n digits
        reg = '^\d{4,}$'
        line = '12345'
        items = re.findall(reg, line)
        self.assertEquals(items, [12345])
        # number with m to n digits
        reg = '^\d{4,5}$'
        line = '12345'
        items = re.findall(reg, line)
        self.assertEquals(items, [12345])

        # startwith zero or not number
        reg = '^(0|[1-9][0-9]*)$'

        # startswith non zero with 2 decimals
        reg = '^([1-9][0-9]*)+(.[0-9]{1,2})?$'
        # plus/minus with 2 decimals
        reg = '^(\-)?\d+(\.\d{1,2})?$'
        # plus/minus and decimals
        reg = '^(\-|\+)?\d+(\.\d+)?$'
        # plus real number with 2 decimals
        reg = '^[0-9]+(\.[0-9]{2})?$'
        # real number with 1-3 decimals
        reg = '^[0-9]+(\.[0-9]{1,3})?$'
        # non-zero positive integer
        reg = '^[1-9]\d*'
        reg = '^\+?[1-9][0-9]*$'
        # non-zero negative integer
        # reg = '([1-9][0-9]*)1,3'

        reg = '^\-[1-9][]0-9"*'
        reg = '-[1-9]\d*'
        # non-negative integer
        reg = '^\d+'
        reg = '[1-9]\d*|0'

        # non-positive integer
        reg = '^-[1-9]\d*|0'
        reg = '((-\d+)|(0+))'

        # non-negative float
        reg = '^\d+(\.\d+)?'
        reg = '[1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0'

        # non-positive float
        reg = '^((-\d+(\.\d+)?)|(0+(\.0+)?))'
        reg = '(-([1-9]\d*\.\d*|0\.\d*[1-9]\d*))|0?\.0+|0'
        # positive float
        reg = '^[1-9]\d*\.\d*|0\.\d*[1-9]\d*或(([0−9]+\.[0−9]∗[1−9][0−9]∗)|([0−9]∗[1−9][0−9]∗\.[0−9]+)|([0−9]∗[1−9][0−9]∗))'
        # negative float
        reg = '^-([1-9]\d*\.\d*|0\.\d*[1-9]\d*)或(−(([0−9]+\.[0−9]∗[1−9][0−9]∗)|([0−9]∗[1−9][0−9]∗\.[0−9]+)|([0−9]∗[1−9][0−9]∗)))'

    def test_float(self):
        # float
        reg = '^(-?\d+)(\.\d+)?'
        reg = '−?([1−9]\d∗\.\d∗|0\.\d∗[1−9]\d∗|0?\.0+|0)'
        self.assertTrue(reg)

    def test_ascii(self):
        # chinese char
        reg = '^[\u4e00-\u9fa5]{0,}$'
        # words
        reg = '^[A-Za-z0-9]+或[A−Za−z0−9]4,40'

        # 长度为3-20的所有字符：
        reg = '^.{3,20}$'

        # alpha string
        reg = '^[A-Za-z]+$'
        # alpha string in upper case
        reg = '^[A-Z]+$'
        # alpha lower case
        reg = '^[a-z]+$'
        # alpha and number
        reg = '^[A-Za-z0-9]+$'
        # number/alpha, _,
        reg = '^\w+或\w3,20'
        # chinese/alpah/number/_
        reg = '^[\u4E00-\u9FA5A-Za-z0-9_]+$'
        # chinese/alpah/digit but withou _
        reg = '^[\u4E00-\u9FA5A-Za-z0-9]+或[\u4E00−\u9FA5A−Za−z0−9]2,20'

        # input contains ^%&',;=?$\"
        reg = '[^%&\',;=?$\x22]+'
        # forbidden ~
        reg = '[^~\x22]+'
        self.assertTrue(reg)

    def test_special_needs(self):
        # email
        reg = '^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'

        # domain
        reg = '[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(/.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+/.?'
        # url
        reg = '[a-zA-z]+://[^\s]*'
        reg = '^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$'
        # cell number China
        reg = '^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'
        # phone
        reg = '("XXX-XXXXXXX"、"XXXX-XXXXXXXX"、"XXX-XXXXXXX"、"XXX-XXXXXXXX"、"XXXXXXX"和"XXXXXXXX)：^(\(\d{3,4}-)|\d{3.4}-)?\d{7,8}$'
        # China phone
        reg = '(0511-4405222、021-87888822)：\d{3}-\d{8}|\d{4}-\d{7}'

        # phone - cell/ 3,4 digits area code, 7,8 digits direct dial, 1-4 extension
        reg = '((\d{11})|^((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1}))$)'
        # China ID - 15, 18 digits, last char might be digit or X
        reg = '(^\d{15})|(\d18)|(^\d{17}(\d|X|x)$)'

        # account number startswith alpha/5-16 length, allow _
        reg = '^[a-zA-Z][a-zA-Z0-9_]{4,15}$'
        # passwd startwith alpha, 6-18 len, alpha digit _
        reg = '^[a-zA-Z]\w{5,17}$'

        # passwd - 8-10 len, alpha digit, no special chars
        reg = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$'
        # date
        reg = '^\d{4}-\d{1,2}-\d{1,2}'
        # months in a year
        reg = '^(0?[1-9]|1[0-2])$'

        # days in a month
        reg = '^((0?[1-9])|((1|2)[0-9])|30|31)$'
        self.assertTrue(reg)

    def test_money(self):
        """
        10000.00/10,000.00/10000, 10,000
        """
        reg = '^[1-9][0-9]*$'
        # not started with zero
        reg = '^(0|[1-9][0-9]*)$'
        # allow zero or minus
        reg = '^(0|-?[1-9][0-9]*)$'
        # allow  zero but not minus
        reg = '^[0-9]+(.[0-9]+)?$'

        # allow 10 or 10.2, not more
        reg = '^[0-9]+(.[0-9]{2})?$'

        # 2 decimals
        reg = '^[0-9]+(.[0-9]{1,2})?$'

        # 1 decimal place
        reg = '^[0-9]{1,3}(,[0-9]{3})*(.[0-9]{1,2})?$'

        # allow ,
        reg = '^([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(.[0-9]{1,2})?$'

        # xml文件：
        reg = '^([a-zA-Z]+-?)+[a-zA-Z0-9]+\\.[x|X][m|M][l|L]$'
        # 中文字符的正则表达式：
        reg = '[\u4e00-\u9fa5]'
        # 双字节字符：
        reg = '[^\x00-\xff]'
        # (包括汉字在内，可以用来计算字符串的长度(一个双字节字符长度计2，ASCII字符计1))
        # 空白行的正则表达式：
        reg = '\n\s*\r'
        # (可以用来删除空白行)
        # HTML标记的正则表达式：
        reg = '<(\S*?)[^>]*>.*?|<.*? />'
        # ( 首尾空白字符的正则表达式：
        reg = '^\s*|\s*'
        reg = '(\s∗)|(\s∗)'
        # (可以用来删除行首行尾的空白字符(包括空格、制表符、换页符等等)，非常有用的表达式)

        # telcent QQ number from 10000
        reg = '[1-9][0-9]{4,}'
        # china post code
        reg = '[1-9]\d{5}(?!\d)'

        # ip：
        reg = '((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))'
        self.assertTrue(reg)
