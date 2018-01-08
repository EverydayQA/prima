#!/usr/bin/python
import re


class RestaurantName():

    def __init__(self, input_contents):
        self.name = input_contents
        if re.match("^[A-Za-z0-9_-]*$", self.name):
            self.no_space_name = self.name.replace(' ', '')
            if str.isalpha(self.no_space_name):
                pass
            else:
                raise ValueError('There are non alphabetic characters that I can not recognize!')

        else:
            raise TypeError('Not String! The input is supposed to be a string type!')

    def __repr__(self):
        return 'RestaurantName(%s)' % self.name.strip()

    def __str__(self):
        return self.name.strip()
