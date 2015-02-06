# Test of Titans

Generating large inputs for programming contests should not be a pain in the @$$.
Test of Titans (TM) will help you generate as many test cases as needed and as
large as specified.

Unfortunately, this will not help you verify the correctness of your solution.
It's a contest right? ;)

# Usage

Pass a JSON file that contains the specifications of your test input. Example,

    {
        "case-count": 8,
        "include-case-count": true,
    }

# Types and related attributes

`int` - Integer value.

- `min` - **Required.** Minimum possible value.
- `max` - **Required.** Maximum possible value.

`float` - Floating point type.

- `min` - **Required.** Minimum possible value.
- `max` - **Required.** Maximum possible value.
- `precision` - **Default is whatever is set for your Python interpreter.** How
many digits go after the decimal point?

`str` - String value.

- `charset` - **Alphanumeric lowercase by default.** Enumerate all the possible
characters allowed in the string.
- `min-len` - **1 by default.** Minimum possible length of the string generated.
- `max-len` - **Required.** Maximum possible length of the string generated.

`int-list` - List of integers.

- `min` - **Required.** Minimum possible value
- `max` - **Required.** Maximum possible value
- `delimiter` - **Space by default.** The delimiter to separate the items of the list.
- `count` - **Required.** The number of items in this list.
- `varlabel` - **Optional, null by default**. In case you want to refer to this
list later.

`float-list` - List of floats.

- `min` - **Required.** Minimum possible value.
- `max` - **Required.** Maximum possible value.
- `precision` - **Default is whatever is set for your Python interpreter.** How
many digits go after the decimal point?
- `delimiter` - **Space by default.** The delimiter to separate the items of the list.
- `count` - **Required.** The number of items in this list.
- `varlabel` - **Optional, null by default**. In case you want to refer to this
list later.

`str-list` - List of strings.

- `charset` - **Alphanumeric lowercase by default.** Enumerate all the possible
characters allowed in the string.
- `min-len` - **1 by default.** Minimum possible length of the string generated.
- `max-len` - **Required.** Maximum possible length of the string generated.
- `delimiter` - **Space by default.** The delimiter to separate the items of the list.
- `count` - **Required.** The number of items in this list.
- `varlabel` - **Optional, null by default**. In case you want to refer to this
list later.

