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
available types for test.

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
four new attributes: `delimiter`, `count`, `sort-by`, and `varlabel`.

`int-list` - List of integers.

- `min` - **Required.** Minimum possible value
- `max` - **Required.** Maximum possible value
- `delimiter` - **Space by default.** The delimiter to separate the items of the list.
- `count` - **Required.** The number of items in this list.
- `sort-by` - **Optional; if unspecified, output is not sorted**. Either `"asc"`
or `"desc"`.
- `varlabel` - **Optional, null by default**. In case you want to refer to this
list later.

`float-list` - List of floats.

- `min` - **Required.** Minimum possible value.
- `max` - **Required.** Maximum possible value.
- `precision` - **Default is whatever is set for your Python interpreter.** How
many digits go after the decimal point?
- `delimiter` - **Space by default.** The delimiter to separate the items of the list.
- `count` - **Required.** The number of items in this list.
- `sort-by` - **Optional; if unspecified, output is not sorted**. Either `"asc"`
or `"desc"`.
- `varlabel` - **Optional, null by default**. In case you want to refer to this
list later.

`str-list` - List of strings.

- `charset` - **Alphanumeric lowercase by default.** Enumerate all the possible
characters allowed in the string.
- `min-len` - **1 by default.** Minimum possible length of the string generated.
- `max-len` - **Required.** Maximum possible length of the string generated.
- `delimiter` - **Space by default.** The delimiter to separate the items of the list.
- `count` - **Required.** The number of items in this list.
- `sort-by` - **Optional; if unspecified, output is not sorted**. Either `"asc"`
or `"desc"`.
- `varlabel` - **Optional, null by default**. In case you want to refer to this
list later.

## Reference type

The reference type produce the same output as atomic types but it is guaranteed
that their value can be found in a previously declared list type. Selection is
done (pseudo-)randomly.

To use a previously declared list type, the particular list type must have a
`varlabel` declared. An error will be thrown if you use an undeclared `varlabel`.

`ref` - A value from some previously-declared list type.

- `varlabel` - **Required.** The corresponding `varlabel` of the list type from
which we pick a value in random.
