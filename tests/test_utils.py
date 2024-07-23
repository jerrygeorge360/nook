import unittest
from nook.utils import HashMap


class TestHashMap(unittest.TestCase):

    def setUp(self):
        self.hashmap = HashMap()

    def test_set_and_get(self):
        self.hashmap.set('key1', 'value1')
        self.assertEqual(self.hashmap.get('key1'), 'value1')

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.hashmap.get('nonexistent'))

    def test_remove_item(self):
        self.hashmap.set('key1', 'value1')
        self.hashmap.remove_item('key1')
        self.assertIsNone(self.hashmap.get('key1'))

    def test_remove_nonexistent_item(self):
        self.hashmap.remove_item('nonexistent')  # Should not raise an exception


if __name__ == '__main__':
    unittest.main()
