import unittest
from click.testing import CliRunner
from nook.main import cli
from nook.utils import HashMap
import pickle


class TestCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_add_command(self):
        result = self.runner.invoke(cli, ['add', '--key', 'key1', '--value', 'value1'])
        self.assertIn('added key-pair', result.output)
        self.assertEqual(result.exit_code, 0)

        # Check if the key-value pair is stored
        with open('hashmap.pickle', 'rb') as f:
            hashmap = pickle.load(f)
            self.assertEqual(hashmap.get('key1'), 'value1')

    def test_delete_command(self):
        hashmap = HashMap()
        hashmap.set('key1', 'value1')
        with open('hashmap.pickle', 'wb') as f:
            pickle.dump(hashmap, f)

        result = self.runner.invoke(cli, ['delete', '--delete', 'key1'])
        self.assertIn('deleted pair', result.output)
        self.assertEqual(result.exit_code, 0)

        # Check if the key-value pair is removed
        with open('hashmap.pickle', 'rb') as f:
            hashmap = pickle.load(f)
            self.assertIsNone(hashmap.get('key1'))


if __name__ == '__main__':
    unittest.main()
