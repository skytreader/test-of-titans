# Test of Titans

[![Build Status](https://travis-ci.org/skytreader/test-of-titans.svg?branch=master)](https://travis-ci.org/skytreader/test-of-titans)
[![Coverage Status](https://coveralls.io/repos/skytreader/test-of-titans/badge.svg?branch=master)](https://coveralls.io/r/skytreader/test-of-titans?branch=master)

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
        "case-format":[
            {"type": "int-list", "min":0, "max":1000000, "count":2, "sort-by":asc"}
        ]
    }

`case-count` specifies how many test cases to generate.

`include-case-count` is a boolean flag that specifies whether we include the
`case-count` in the output or not.

`case-format` describes a test case. The value is a list, containing specifications
on the lines that will comprise the test case. The possible values are described
in the next section.

# Types and related attributes

Every line in a test case is a particular type. This section explains the
available types for test and their attributes.

Every type, atomic or list, can have the following attributes:

- `repeat` - **1 by default.** Should always be an integer value greater than 1.
Specifies how many times to print out this particular type, once per line. Useful
for test inputs made up of _n_ sections of data, where each section has a
property that can be described by a particular attribute set.

## Atomic types

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

**Note:** For fixed-length strings, just specify the same `min-len` and `max-len`.

## List types

List types allow you to group atomic types in a single line. Their type key is
the same as their atomic counterparts _but_ appended with `-list`. They feature
four new attributes as described below.

- `delimiter` - **Space by default.** The delimiter to separate the items of the list.
- `count` - **Required.** The number of items in this list.
- `sort-by` - **Optional; if unspecified, output is not sorted.** Either `"asc"`
or `"desc"`.
- `varlabel` - **Optional, null by default.** In case you want to refer to this
list later.
- `is-not` - **Optional, null by default.** The `varlabel` of another list which
_will not be_ equal to this list.
- `not-in` - **Optional, null by default.** The `varlabel` of another list
which makes it so that none of the items in the referred list is similar to the
items in this new llist.

`int-list` - List of integers.

- `min` - **Required.** Minimum possible value
- `max` - **Required.** Maximum possible value

`float-list` - List of floats.

- `min` - **Required.** Minimum possible value.
- `max` - **Required.** Maximum possible value.
- `precision` - **Default is whatever is set for your Python interpreter.** How
many digits go after the decimal point?

`str-list` - List of strings.

- `charset` - **Alphanumeric lowercase by default.** Enumerate all the possible
characters allowed in the string.
- `min-len` - **1 by default.** Minimum possible length of the string generated.
- `max-len` - **Required.** Maximum possible length of the string generated.

## Reference type

The reference type produces the same output as atomic types but it is guaranteed
that their value can be found in a previously declared list type. Selection is
done (pseudo-)randomly.

To use a previously declared list type, the particular list type must have a
`varlabel` declared. An error will be thrown if you use an undeclared `varlabel`.

`ref` - A value from some previously-declared list type.

- `varlabel` - **Required.** The corresponding `varlabel` of the list type from
which we pick a value in random.

# License

MIT
