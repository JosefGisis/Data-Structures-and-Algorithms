HEX_DECIMAL_SET: list[int | str] = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
]

HEX_BASE = 16


def base_ten_to_hex(base_ten: int):
    result: str = ""
    quotient: int = abs(base_ten)
    while quotient >= HEX_BASE:
        remainder: int = quotient % HEX_BASE
        quotient = quotient // HEX_BASE

        result = f"{HEX_DECIMAL_SET[remainder]}{result}"
    sign: str = "-" if base_ten < 0 else ""
    return f"{sign}{HEX_DECIMAL_SET[quotient]}{result}"


for n in [0, 1, 9, 10, 16, 15, -20, 16, 17, 255, 256, 271, 272, 2345, 4096, 65535]:
    result = base_ten_to_hex(n)
    print(result)
    assert result == format(n, "x"), n
