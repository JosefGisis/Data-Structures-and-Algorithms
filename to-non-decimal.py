from digit_maps import (
    BINARY_DIGIT_MAP,
    BINARY_RADIX,
    HEX_DIGIT_MAP,
    HEX_RADIX,
    DigitMap,
)


class NonDecimalResult:
    def __init__(self, radix: int, digit_map: DigitMap, is_negative: bool = False):
        self.result = ""
        self.radix = radix
        self.digit_map = digit_map
        self.is_negative = is_negative

    def add_next_digit(self, value: int) -> None:
        if value >= self.radix:
            raise ValueError(
                "Cannot provide a value at add_next_digit that is equal to or greater than the radix"
            )
        digit: str | int = self.digit_map[value]
        self.result = f"{digit}{self.result}"

    def to_result(self) -> str:
        sign = "-" if self.is_negative else ""
        return f"{sign}{self.result}"


def to_non_decimal(value: int, radix: int, digit_map: DigitMap) -> str:
    if radix < 2:
        raise ValueError("radix must be a value that is greater than or equal to 2")
    if not radix == len(digit_map):
        raise ValueError("digit map size must match the provided radix")

    is_negative = value < 0
    quotient = abs(value)

    result = NonDecimalResult(radix, digit_map, is_negative)

    while quotient >= radix:
        remainder = quotient % radix
        quotient = quotient // radix
        result.add_next_digit(remainder)

    result.add_next_digit(quotient)

    return result.to_result()


print("Test convert to hex")

for n in [0, 1, 9, 10, 16, 15, -20, 16, 17, 255, 256, 271, 272, 2345, 4096, 65535]:
    result = to_non_decimal(n, HEX_RADIX, HEX_DIGIT_MAP)
    print(result)
    assert result == format(n, "x"), n

print("Test convert to binary")

for n in [0, 1, 9, 10, 16, 15, -20, 16, 17, 255, 256, 271, 272, 2345, 4096, 65535]:
    result = to_non_decimal(n, BINARY_RADIX, BINARY_DIGIT_MAP)
    print(result)
    assert result == format(n, "b"), n
