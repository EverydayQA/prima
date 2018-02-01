#!/usr/bin/python
import re


class RestaurantName():
    """
    Normalize Name
    """

    def __init__(self, input_contents):
        self.name = self.normalize_name(input_contents)

    def __repr__(self):
        return 'RestaurantName(%s)' % self.name.strip()

    def __str__(self):
        return self.name.strip()

    def normalize_name(self, name):
        """
        Returns rename that is valid

        :return: No space name
        :rtype: basestring
        :exception: if not valid
        """
        if re.match("^[A-Za-z0-9_-]*$", name):
            no_space_name = name.replace(' ', '')
            if str.isalpha(no_space_name):
                return no_space_name
            raise ValueError('There are non alphabetic characters that I can not recognize!')

        else:
            raise TypeError('Not String! The input is supposed to be a string type!')

        return name
