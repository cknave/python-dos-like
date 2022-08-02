import unittest

from dos_like import int_with_flags


class TestIntWithFlags(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.enum = int_with_flags.IntWithFlags('enum', {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'flag1': 4,
            'flag2': 8,
        })
        self.enum._flags_ = {'flag1': 4, 'flag2': 8}

    def test_values_are_correct(self):
        self.assertEqual(0, self.enum.zero.value)
        self.assertEqual(1, self.enum.one.value)
        self.assertEqual(2, self.enum.two.value)
        self.assertEqual(3, self.enum.three.value)

    def test_flags_are_correct(self):
        self.assertEqual(4, self.enum.flag1.value)
        self.assertEqual(8, self.enum.flag2.value)

    def test_single_flag_combination(self):
        self.assertEqual(4 | 0, self.enum.flag1 | self.enum.zero)
        self.assertEqual(4 | 1, self.enum.flag1 | self.enum.one)
        self.assertEqual(4 | 2, self.enum.flag1 | self.enum.two)
        self.assertEqual(4 | 3, self.enum.flag1 | self.enum.three)
        self.assertEqual(8 | 0, self.enum.flag2 | self.enum.zero)
        self.assertEqual(8 | 1, self.enum.flag2 | self.enum.one)
        self.assertEqual(8 | 2, self.enum.flag2 | self.enum.two)
        self.assertEqual(8 | 3, self.enum.flag2 | self.enum.three)

    def test_multiple_flag_combination(self):
        self.assertEqual(8 | 4 | 0,
                         self.enum.flag2 | self.enum.flag1 | self.enum.zero)

    def test_invalid_flag_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.enum(16)

    def test_flag_or_int(self):
        self.assertEqual(4 | 1, 4 | self.enum.one)

    def test_flag_or_with_non_int_raises_type_error(self):
        with self.assertRaises(TypeError):
            _ = self.enum.zero | 'oh no'

    def test_single_flag_combination_name(self):
        self.assertEqual('three|flag1',
                         (self.enum.three | self.enum.flag1).name)

    def test_multiple_flag_combination_name(self):
        self.assertEqual(
            'three|flag1|flag2',
            (self.enum.three | self.enum.flag1 | self.enum.flag2).name,
        )
