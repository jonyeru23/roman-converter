

class RomanSymbols:
    def __init__(self):
        self.__roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        self.__keys_in_order = [
            'M',
            'D',
            'C',
            'L',
            'X',
            'V',
            'I'
        ]

    def get_keys_in_order(self):
        return self.__keys_in_order

    def get_roman_values(self):
        return self.__roman_values


class ErrorChecker:
    @staticmethod
    def _is_int(questionable_int, var_name):
        if type(questionable_int) is int:
            return True
        else:
            print(type(questionable_int))
            raise TypeError(f'The {var_name} must be an int')

    @staticmethod
    def _is_it_too_long(questionable_length):
        if questionable_length < 5:
            return questionable_length
        else:
            raise UserWarning(f"The number to convert is too long can't calculate")


class Calculator(ErrorChecker):
    def __init__(self, number_to_convert):
        self.the_num = number_to_convert
        self.roman = RomanSymbols()
        self.roman_values = self.roman.get_roman_values()
        self.roman_keys = self.roman.get_keys_in_order()
        self.new_string = ''

    def _make_string(self):
        if self._is_int(self.the_num, 'number_to_convert'):
            return str(self.the_num)

    def _get_length(self):
        return len(self._make_string())

    def make_roman(self):
        for power_of in reversed(range(self._is_it_too_long(self._get_length()))):
            part_of_num = self._get_dec(power_of)
            self._division(part_of_num)
            self.the_num -= part_of_num

        return self.new_string

    def _get_dec(self, power_of):
        return self.the_num - (self.the_num % pow(10, power_of))

    def _division(self, part_of_num):
        for index, symbol in enumerate(self.roman_keys):
            times = self._how_many_times(part_of_num, self.roman_values[symbol])
            if times == 0 and self._check_for_nine(part_of_num, self.roman_values[symbol]):
                self.new_string += self.roman_keys[index + 2]
                self.new_string += symbol
                break

            elif self._is_between_4_and_0(times):
                self._add_to_string(times, symbol)
                if self._is_bigger_than_5(times):
                    self._division(self._remainder(part_of_num, self.roman_values[symbol]))
                break

            elif self._is_it_four(times):
                self.new_string += symbol
                self.new_string += self.roman_keys[index - 1]

            elif self._is_it_a_big_num(times, symbol):
                self._add_to_string(times, symbol)

    @staticmethod
    def _is_bigger_than_5(times):
        return times == 1

    @staticmethod
    def _is_between_4_and_0(times):
        return 0 < times < 4

    @staticmethod
    def _is_it_four(times):
        return times == 4

    @staticmethod
    def _is_it_a_big_num(times, symbol):
        return times > 4 and symbol == 'M'

    def _add_to_string(self, times, symbol):
        for _ in range(times):
            self.new_string += symbol

    @staticmethod
    def _how_many_times(part_of_num, roman_num):
        return part_of_num // roman_num

    @staticmethod
    def _remainder(part_of_num, roman_num):
        return part_of_num % roman_num

    @staticmethod
    def _check_for_nine(part_of_num, roman_num):
        return part_of_num / roman_num == 0.9
    
