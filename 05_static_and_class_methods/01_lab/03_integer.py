



class Integer:
    ROMAN_NUMERALS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        int_value = 0
        previous_value = 0
        for char in reversed(value):
            current_value = cls.ROMAN_NUMERALS[char]

            if current_value < previous_value:
                int_value -= current_value

            else:
                int_value += current_value
            previous_value = current_value
        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"

        try:
            return cls(int(value))

        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
