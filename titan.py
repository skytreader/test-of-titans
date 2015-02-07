#! /usr/bin/env python3

import random
import string

class Titan(object):
    
    def __init__(self):
        pass

    def __int(self, mini, maxi):
        return random.randint(mini, maxi)
    
    def __float(self, mini, maxi, precision=None):
        # TODO Precision!
        return random.uniform(mini, maxi)

    def __str(self, maxlen, minlen=1, charset=None):
        charset = charset if charset else "".join((string.lowercase, string.digits))
        # TODO minlen!
        return "".join([random.choice(charset) for _ in range(maxlen)])
