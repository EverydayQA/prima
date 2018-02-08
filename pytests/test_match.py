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
        line = 'test_m_m_ff_ss__mmm.txt'
        matches = re.findall(regex, line)
        self.assertEquals(matches, ['test', 'm', 'm', 'ff', 'ss'])
        matches = re.split('_+', line)
        self.assertEquals(matches, ['test', 'm', 'm', 'ff', 'ss', 'mmm.txt'])
