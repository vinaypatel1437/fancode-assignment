import unittest
from src.fancode_logic import calculate_completion_percentage, is_user_in_fancode_city

class TestFanCodeLogic(unittest.TestCase):

    def test_calculate_completion_percentage(self):
        todos = [
            {'userId': 1, 'completed': True},
            {'userId': 1, 'completed': False},
            {'userId': 1, 'completed': True}
        ]
        result = calculate_completion_percentage(todos, 1)
        self.assertEqual(result, 66.67)

    def test_is_user_in_fancode_city(self):
        user_in_fancode = {'address': {'geo': {'lat': '-10', 'lng': '50'}}}
        user_not_in_fancode = {'address': {'geo': {'lat': '-50', 'lng': '150'}}}
        
        self.assertTrue(is_user_in_fancode_city(user_in_fancode))
        self.assertFalse(is_user_in_fancode_city(user_not_in_fancode))

if __name__ == '__main__':
    unittest.main()
