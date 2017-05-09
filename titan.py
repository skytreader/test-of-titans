#! /usr/bin/env python3

import json
import random
import string
import sys

class Titan(object):
    
    def __init__(self):
        self.type_map = dict()
        self.type_map["int"] = self.__int
        self.type_map["float"] = self.__float
        self.type_map["str"] = self.__str
        self.type_map["int-list"] = self.__intlist
        self.type_map["float-list"] = self.__floatlist
        self.type_map["str-list"] = self.__strlist
        self.type_map["ref"] = self.__ref

        self.arg_mapping = dict()
        # Map the specified attribute to the name of the argument.
        self.arg_mapping["int"] = {"min":"mini", "max":"maxi"}
        self.arg_mapping["float"] = {"min":"mini", "max":"maxi",
          "precision":"precision"}
        self.arg_mapping["str"] = {"charset":"charset", "min-len":"minlen",
          "max-len":"maxlen"}
        self.arg_mapping["int-list"] = {"min":"mini", "max":"maxi",
          "delimiter":"delimiter", "count":"count", "sort-by":"sort_by",
          "varlabel":"varlabel"}
        self.arg_mapping["float-list"] = {"min":"mini", "max":"maxi",
          "delimiter":"delimiter", "count":"count", "sort-by":"sort_by",
          "varlabel":"varlabel", "precision":"precision"}
        self.arg_mapping["str-list"] = {"charset":"charset", "min-len":"minlen",
          "max-len":"maxlen", "delimiter":"delimiter", "count":"count",
          "sort-by":"sort_by", "varlabel":"varlabel"}
        self.arg_mapping["ref"] = {"varlabel":"varlabel"}

        # Contains all the lists for our reference type
        # This will be a mapping of varlabels to the list generated
        self.reftype_lookup = {}

    def __int(self, mini, maxi):
        return random.randint(mini, maxi)
    
    def __float(self, mini, maxi, precision=None):
        # TODO Precision!
        return random.uniform(mini, maxi)

    def __str(self, maxlen, minlen=1, charset=None):
        charset = charset if charset else "".join((string.ascii_lowercase, string.digits))
        return "".join([random.choice(charset) for _ in range(random.randint(minlen, maxlen))])

    def __lister(self, atom_fun, atom_args, count, delimiter=None, sort_by=None,
      varlabel=None):
        delimiter = delimiter if delimiter else " "
        ls = [atom_fun(**atom_args) for _ in range(count)]

        if sort_by:
            ls.sort(reverse = (sort_by == "desc"))

        print_ls = delimiter.join(list(map(str, ls)))

        if varlabel:
            self.reftype_lookup[varlabel] = ls

        return print_ls

    def __intlist(self, mini, maxi, count, delimiter=None, sort_by=None, varlabel=None):
        return self.__lister(self.__int, {"maxi":maxi, "mini":mini}, count,
          delimiter, sort_by, varlabel)

    def __floatlist(self, mini, maxi, count, precision=None, delimiter=None,
      sort_by=None, varlabel=None):
        return self.__lister(self.__float, {"maxi":maxi, "mini":mini,
          "precision":precision}, count, delimiter, sort_by, varlabel)

    def __strlist(self, maxlen, count, minlen=1, charset=None, delimiter=None,
      sort_by=None, varlabel=None):
        return self.__lister(self.__str, {"maxlen":maxlen, "minlen":minlen,
          "charset":charset}, count, delimiter, sort_by, varlabel)

    def __ref(self, varlabel):
        prevls = self.reftype_lookup[varlabel]
        return str(random.choice(prevls))

    def interpret(self, rule):
        """
        Pass the type maps here. Note: pass Python dicts, not JSON maps for
        parsing.
        """
        generator_method = self.type_map[rule["type"]]
        arglist = self.arg_mapping[rule["type"]]
        constructed_args = {}

        for jspec_key in arglist.keys():
            constructed_args[arglist[jspec_key]] = rule.get(jspec_key)

        return generator_method(**constructed_args)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "spec.json")
        exit(1)

    with open(sys.argv[1]) as json_spec:
        spec = json.load(json_spec)
        titan = Titan()
        
        if spec["include-case-count"]:
            print(spec["case-count"])

        for i in range(spec["case-count"]):
            for rule in spec["case-format"]:
                print(titan.interpret(rule))
