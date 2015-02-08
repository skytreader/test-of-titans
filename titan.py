#! /usr/bin/env python3

import random
import string

class Titan(object):
    # TODO Note of varlabel!
    
    def __init__(self):
        self.type_map = dict()
        self.type_map["int"] = self.__int
        self.type_map["float"] = self.__float
        self.type_map["str"] = self.__str
        self.type_map["int-list"] = self.__intlist
        self.type_map["float-list"] = self.__floatlist
        self.type_map["str-list"] = self.__strlist

        self.arg_mapping = dict()
        # Map the specified attribute to the name of the argument/
        self.arg_mapping["int"] = {"min":"mini", "max":"maxi"}

    def __int(self, mini, maxi):
        return str(random.randint(mini, maxi))
    
    def __float(self, mini, maxi, precision=None):
        # TODO Precision!
        return str(random.uniform(mini, maxi))

    def __str(self, maxlen, minlen=1, charset=None):
        charset = charset if charset else "".join((string.lowercase, string.digits))
        # TODO minlen!
        return "".join([random.choice(charset) for _ in range(maxlen)])

    def __intlist(self, mini, maxi, count, delimiter=" ", sort_by=None, varlabel=None):
        ints = [self.__int(mini, maxi) for _ in range(count)]

        if sort_by:
            ints.sort(reverse, reverse = (sort_by == "desc"))

        return delimiter.join(list(map(str, ints)))

    def __floatlist(self, mini, maxi, count, precision=None, delimiter=" ",
      sort_by=None, varlabel=None):
        floats = [self.__float(mini, maxi, precision) for _ in range(count)]

        if sort_by:
            floats.sort(reverse, reverse = (sort_by == "desc"))

        return delimiter.join(list(map(str, floats)))

    def __strlist(self, maxlen, count, minlen=1, charset=None, delimiter=" ",
      sort_by=None, varlabel=None):
        strings = [self.__str(maxlen, minlen, charset) for _ in range(count)]

        if sort_by:
            strings.sort(reverse, reverse = (sort_by == "desc"))

        return delimiter.join(strings)

    def interpret(self, rule):
        """
        Pass the type maps here. Note: pass Python dicts, not JSON maps for
        parsing.
        """
        generator_method = self.type_map[rule["type"]]
        arglist = self.arg_mapping[rult["type"]]
        constructed_args = {}

        for jspec_key in arglist.keys():
            constructed_args[arglist[jspec_key]] = rule[jspec_key]

        return generator_method(**constructed_args)
