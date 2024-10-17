import unittest
import tap_swap


class test_tap_swap(unittest.TestCase):
	def test_that_the_tap_swap_elements_exit_in_the_list(self):
		tap_swap.get_swapped_elements([1, 1, 1, 1, 1, 1])

	def test_that_get_swapped_elements_function_returns_swapped_elements(self):

		array_to_be_swapped = [1, 2, 3, 4, 5, 6]
		expected_output = [2, 1, 4, 3, 6, 5]
		self.assertEqual(tap_swap.get_swapped_elements(array_to_be_swapped), expected_output)

