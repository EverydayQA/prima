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
        # m-n位的数字：
        reg = '^\d{4,5}$'
        line = '12345'
        items = re.findall(reg, line)
        self.assertEquals(items, [12345])


"""
    零和非零开头的数字：^(0|[1-9][0-9]*)$
    非零开头的最多带两位小数的数字：^([1-9][0-9]*)+(.[0-9]{1,2})?$
    带1-2位小数的正数或负数：^(\-)?\d+(\.\d{1,2})?$
    正数、负数、和小数：^(\-|\+)?\d+(\.\d+)?$
    有两位小数的正实数：^[0-9]+(\.[0-9]{2})?$
    有1~3位小数的正实数：^[0-9]+(\.[0-9]{1,3})?$
    非零的正整数：^[1-9]\d*或([1−9][0−9]∗)1,3

或 ^\+?[1-9][0-9]*$
非零的负整数：^\-[1-9][]0-9"*或−[1−9]\d∗
非负整数：^\d+或[1−9]\d∗|0
非正整数：^-[1-9]\d*|0或((−\d+)|(0+))
非负浮点数：^\d+(\.\d+)?或[1−9]\d∗\.\d∗|0\.\d∗[1−9]\d∗|0?\.0+|0
非正浮点数：^((-\d+(\.\d+)?)|(0+(\.0+)?))或(−([1−9]\d∗\.\d∗|0\.\d∗[1−9]\d∗))|0?\.0+|0
正浮点数：^[1-9]\d*\.\d*|0\.\d*[1-9]\d*或(([0−9]+\.[0−9]∗[1−9][0−9]∗)|([0−9]∗[1−9][0−9]∗\.[0−9]+)|([0−9]∗[1−9][0−9]∗))
负浮点数：^-([1-9]\d*\.\d*|0\.\d*[1-9]\d*)或(−(([0−9]+\.[0−9]∗[1−9][0−9]∗)|([0−9]∗[1−9][0−9]∗\.[0−9]+)|([0−9]∗[1−9][0−9]∗)))
浮点数：^(-?\d+)(\.\d+)?或−?([1−9]\d∗\.\d∗|0\.\d∗[1−9]\d∗|0?\.0+|0)
"""

    def test_ascii(self):
        """
        # chinese char
        reg = '^[\u4e00-\u9fa5]{0,}$'
        # words
        reg = '^[A-Za-z0-9]+或[A−Za−z0−9]4,40'

        # 长度为3-20的所有字符：
        reg = '^.{3,20}$'

由26个英文字母组成的字符串：^[A-Za-z]+$
由26个大写英文字母组成的字符串：^[A-Z]+$
由26个小写英文字母组成的字符串：^[a-z]+$
由数字和26个英文字母组成的字符串：^[A-Za-z0-9]+$
由数字、26个英文字母或者下划线组成的字符串：^\w+或\w3,20
中文、英文、数字包括下划线：^[\u4E00-\u9FA5A-Za-z0-9_]+$
中文、英文、数字但不包括下划线等符号：^[\u4E00-\u9FA5A-Za-z0-9]+或[\u4E00−\u9FA5A−Za−z0−9]2,20

    可以输入含有^%&',;=?$\"等字符：[^%&',;=?$\x22]+
    禁止输入含有~的字符：[^~\x22]+
        """

    def test_special_needs(self):
        """
        # email
        reg = '^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$'

        # domain
        reg = '[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(/.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+/.?'

        InternetURL：[a-zA-z]+://[^\s]* 或 ^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$
        手机号码：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
        电话号码("XXX-XXXXXXX"、"XXXX-XXXXXXXX"、"XXX-XXXXXXX"、"XXX-XXXXXXXX"、"XXXXXXX"和"XXXXXXXX)：^(\(\d{3,4}-)|\d{3.4}-)?\d{7,8}$
        国内电话号码(0511-4405222、021-87888822)：\d{3}-\d{8}|\d{4}-\d{7}
        电话号码正则表达式（支持手机号码，3-4位区号，7-8位直播号码，1－4位分机号）: ((\d{11})|^((\d{7,8})|(\d{4}|\d{3})-(\d{7,8})|(\d{4}|\d{3})-(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1})|(\d{7,8})-(\d{4}|\d{3}|\d{2}|\d{1}))$)
        身份证号(15位、18位数字)，最后一位是校验位，可能为数字或字符X：(^\d{15})|(\d18

)|(^\d{17}(\d|X|x)$)
帐号是否合法(字母开头，允许5-16字节，允许字母数字下划线)：^[a-zA-Z][a-zA-Z0-9_]{4,15}$
密码(以字母开头，长度在6~18之间，只能包含字母、数字和下划线)：^[a-zA-Z]\w{5,17}$
强密码(必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8-10之间)：^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$
日期格式：^\d{4}-\d{1,2}-\d{1,2}
一年的12个月(01～09和1～12)：^(0?[1-9]|1[0-2])$
一个月的31天(01～09和1～31)：^((0?[1-9])|((1|2)[0-9])|30|31)$
钱的输入格式：

        有四种钱的表示形式我们可以接受:"10000.00" 和 "10,000.00", 和没有 "分" 的 "10000" 和 "10,000"：^[1-9][0-9]*$
    这表示任意一个不以0开头的数字,但是,这也意味着一个字符"0"不通过,所以我们采用下面的形式：^(0|[1-9][0-9]*)$
    一个0或者一个不以0开头的数字.我们还可以允许开头有一个负号：^(0|-?[1-9][0-9]*)$
    这表示一个0或者一个可能为负的开头不为0的数字.让用户以0开头好了.把负号的也去掉,因为钱总不能是负的吧。下面我们要加的是说明可能的小数部分：^[0-9]+(.[0-9]+)?$
    必须说明的是,小数点后面至少应该有1位数,所以"10."是不通过的,但是 "10" 和 "10.2" 是通过的：^[0-9]+(.[0-9]{2})?$
    这样我们规定小数点后面必须有两位,如果你认为太苛刻了,可以这样：^[0-9]+(.[0-9]{1,2})?$
    这样就允许用户只写一位小数.下面我们该考虑数字中的逗号了,我们可以这样：^[0-9]{1,3}(,[0-9]{3})*(.[0-9]{1,2})?$
        1到3个数字,后面跟着任意个 逗号+3个数字,逗号成为可选,而不是必须：^([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(.[0-9]{1,2})?$
    备注：这就是最终结果了,别忘了"+"可以用"*"替代如果你觉得空字符串也可以接受的话(奇怪,为什么?)最后,别忘了在用函数时去掉去掉那个反斜杠,一般的错误都在这里
        """

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
