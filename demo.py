# I am going to be testing my extremely rusty python skills

from typing import Self

a_string: str = "Hello World"
a_number: int = 3
a_floating_point_number: float = 1.5
an_array_of_numbers: list[int] = [4, 5, 6]
a_dictionary_of_string_number_pairs: dict[str, int] = {"key1": 3, "key2": 4}


# define a class
class Cat:
    pet_type = "Cat"

    def __init__(self, pet_name: str):
        self.name = pet_name

    def __add__(self, other_cat: Self) -> str:
        return f"You have created {self.name}{other_cat.name}!"


purry = Cat("Purry")
meowy = Cat("Meowy")
print(purry + meowy)

number_list: list[int] = [4, 6, 3, 6, 7, 1, 7, 3, 2]


def find_highest_number(lst: list[int]) -> int | None:
    highest_number: int = 0
    for number in lst:
        if not highest_number or number > highest_number:
            highest_number = number
    return highest_number


print(find_highest_number(number_list))

double_even_list = [item * 2 if item % 2 == 0 else item for item in number_list]
print(double_even_list)
flat_to_flat = [item for item in number_list]
print(flat_to_flat)
nested_list = [[1, 2, 3], [1, 2]]
flattened_list = [item for sub_list in nested_list for item in sub_list]
print(flattened_list)

# generator function
get_next_squared_number = (x**2 for x in range(100))
print(next(get_next_squared_number))
print(next(get_next_squared_number))
print(next(get_next_squared_number))
print(next(get_next_squared_number))
