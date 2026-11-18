from operator import indexOf

from digit_maps import (
    BINARY_DIGIT_MAP,
    BINARY_RADIX,
    HEX_DIGIT_MAP,
    HEX_RADIX,
    DigitMap,
)


def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def to_decimal(value: str | int, radix: int, digit_map: DigitMap) -> int:
    if radix < 2:
        raise ValueError("radix must be a value that is greater than or equal to 2")
    if not radix == len(digit_map):
        raise ValueError("digit map size must match the provided radix")
    as_list = list(f"{value}".lower())
    is_negative = as_list[0] == "-"
    if is_negative:
        as_list.pop(0)

    value_length = len(as_list)

    if value_length == 0:
        raise ValueError("No value provided")

    as_list.reverse()
    total = 0

    for index, item in enumerate(as_list):
        is_number = is_int(item)
        if is_number:
            item = int(item)
        decimal_value = indexOf(digit_map, item)
        if decimal_value < 0:
            raise ValueError("Invalid map for provided value")
        position_value = decimal_value * radix**index
        total += position_value

    return total if not is_negative else (0 - total)


print(to_decimal("1010", BINARY_RADIX, BINARY_DIGIT_MAP))

print("Test convert from hex")

for n in [0, 1, 9, 10, 16, 15, -20, 16, 17, 255, 256, 271, 272, 2345, 4096, 65535]:
    result = to_decimal(format(n, "x"), HEX_RADIX, HEX_DIGIT_MAP)
    print(result)
    assert result == n, n

print("Test convert from binary")

for n in [0, 1, 9, 10, 16, 15, -20, 16, 17, 255, 256, 271, 272, 2345, 4096, 65535]:
    result = to_decimal(format(n, "b"), BINARY_RADIX, BINARY_DIGIT_MAP)
    print(result)
    assert result == n, n
